import numpy as np
from ltp import LTP
import json
from math import log2
from operator import itemgetter
import sys
sys.path.append("..")
from config import *



class IterateComments:
    def __init__(self, raw_comments):
        self.iter_raw = iter(raw_comments.items())

    def iter_loads_comments(self):
        try:
            value = json.loads(next(self.iter_raw)[1])
            return {  # 'comment_id': value['comment_id'], 'user_id': value['user_id'], 'url_id': value['url_id'],
                'comment_text': value['comment_text'], 'comment_emoji': value['comment_emoji'],
                'like_count': value['like_count'] or 0, 'reply_count': value['reply_count'] or 0,
                'be_co_retweet': value['be_co_retweet'] or 0, 'be_co_comments': value['be_co_comments'] or 0,
                'be_co_like': value['be_co_like'] or 0, 'be_contents': value['be_contents'],
                'be_emoji': value['be_emoji']}
        except StopIteration:
            return False


class ProjectComments:
    """
    负责抽取文本特征
    注意：官方文档
    https://ltp.readthedocs.io/zh_CN/latest/
    有些是”栏得啊毛“的
    """
    def __init__(self, dimension_threshold_role=5, dimension_threshold_dr=8, dimension_threshold_ner=4):
        self.ltp = LTP()
        """
        这个词性标注官方文档不全的 https://ltp.readthedocs.io/zh_CN/latest/appendix.html
        那个代码中有但文档中没有的 'z' 不知道表示什么东东
        """
        self.switch = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'g': 5, 'h': 6, 'i': 7, 'j': 8, 'k': 9, 'm': 10, 'n': 11,
                       'nd': 12, 'nh': 13, 'ni': 14, 'nl': 15, 'ns': 16, 'nt': 17, 'nz': 18, 'o': 19, 'p': 20, 'q': 21,
                       'r': 22, 'u': 23, 'v': 24, 'wp': 25, 'ws': 26, 'x': 27, 'z': 28}
        self.dimension_threshold_role = dimension_threshold_role
        self.dimension_threshold_dr = dimension_threshold_dr
        self.dimension_threshold_ner = dimension_threshold_ner

    def iter_project_quad(self, comment_text, be_contents, like_count, reply_count, be_co_retweet, be_co_comments,
                          be_co_like):
        if len(comment_text) <= 1:
            comment_text = "空"
        if len(be_contents) <= 1:
            be_contents = "废"
        splited = comment_text.split('|')
        seg, hidden = self.ltp.seg(splited)
        be_contents_split = be_contents.split('|')
        be_contents_seg, be_contents_hidden = self.ltp.seg(be_contents_split)
        return comment_text, self._part_of_speech(hidden), self._semantic_role(hidden), \
               self._semantic_dependency_relations(hidden), self._semantic_relationship(seg, hidden, be_contents_seg,
                                                                                        be_contents_hidden), self._heatage(
            like_count, reply_count, be_co_retweet, be_co_comments, be_co_like)

    def _part_of_speech(self, hidden):
        pos = self.ltp.pos(hidden)
        tag_list = [0] * 30
        for sub_vector in pos:
            for tag in sub_vector:
                tag_list[self.switch.get(tag, 29)] += 1
        return tag_list

    def _semantic_role(self, hidden):
        """
        对于句子嵌套结构的复杂度的要求大于句子命名个体的复杂度
        定义每个句子的语义结构复杂度为 ∏ log2(Ni+1)
        """
        srl = self.ltp.srl(hidden, keep_empty=False)
        role_list = [0] * self.dimension_threshold_role
        if len(srl) == 0:
            return role_list
        index = 0
        for sub_role in srl:
            role_len = 1
            if index > (self.dimension_threshold_role - 1):
                return role_list
            for role in sub_role:
                role_len *= log2(len(role[1]) + 1)
            role_list[index] = role_len
            index += 1
        return role_list

    def _semantic_dependency_relations(self, hidden):
        """
        这官方文档像放屁一样：源码里参数都变了，文档里示例还是老的
        得到句子语义依存分析后的树的深度(depth)和每层的宽度(width)
        定义每个句子的复杂度为 Σ depth * log2(width)
        """
        sdp = self.ltp.sdp(hidden, mode="tree")
        dr_list = [0] * self.dimension_threshold_dr
        if len(sdp) == 0:
            return dr_list
        index = 0
        for sub_dr in sdp:
            if index > (self.dimension_threshold_dr - 1):
                return dr_list
            hash_map = {}
            total_weight = 0
            for dr in sub_dr:
                if dr[1] not in hash_map:
                    hash_map[dr[1]] = []
                hash_map[dr[1]].append(dr[0])
            max_width = 0
            for node_value in hash_map.values():
                max_width = max(max_width, len(node_value))
            total_weight += max_width * log2(len(hash_map))
            dr_list[index] = total_weight
            index += 1
        return dr_list

    def _semantic_relationship(self, seg, hidden, be_seg, be_contents_hidden):
        """
        根据命名实体识别，分别识别评论文本与被评论对象的 NE，根据其相似度分析评论的相关性
        就怕水军在评论时搞几个被评论对象中的 NE 来骗，来偷袭
        """
        ner = self.ltp.ner(hidden)
        be_ner = self.ltp.ner(be_contents_hidden)
        relation_list = [0] * self.dimension_threshold_ner
        if len(ner) == 0 or len(be_ner) == 0:  # or (len(ner) == 1 and len(ner[0]))
            return relation_list
        # print(ner)
        ner_loc = 0
        be_ner_loc = 0
        comments_ne = set()
        be_comments_ne = set()
        for sub_ner in ner:
            for comments_ner in sub_ner:
                tag, start, end = comments_ner
                comments_ne.add("".join(seg[ner_loc][start:end + 1]))
            ner_loc += 1
        for sub_be_ner in be_ner:
            for be_comments_ner in sub_be_ner:
                be_tag, be_start, be_end = be_comments_ner
                be_comments_ne.add("".join(be_seg[be_ner_loc][be_start:be_end + 1]))
            be_ner_loc += 1
        relation_list[0] = len(comments_ne)
        relation_list[1] = len(comments_ne & be_comments_ne)
        # print(str(comments_ne) + " || " + str(be_comments_ne))
        return relation_list

    def _heatage(self, like_count, reply_count, be_co_retweet, be_co_comments, be_co_like):
        # print("like_count: " + str(like_count) + " | reply_count: " + str(reply_count) + " | be_co_retweet: " + str(be_co_retweet) +
        #       " | be_co_comments: " + str(be_co_comments) + " | be_co_like: " + str(be_co_like))
        ht = list(map(int, [like_count, reply_count, be_co_retweet, be_co_comments, be_co_like]))
        return ht


if __name__ == '__main__':
    # 从数据库中读出评论
    raw_comments = r.hgetall(raw_comments_db)

    # 使用适当的参数初始化异常检测算法第一层的训练模型
    pj_module = ProjectComments(6, 8, 4)

    # 将评论变为可迭代的
    iter_comment = IterateComments(raw_comments)

    while True:
        misc = iter_comment.iter_loads_comments()
        if not isinstance(misc, bool):
            c = pj_module.iter_project_quad(*itemgetter(*keys)(misc))
            view_judge.append(c)
        else:
            break
    print(np.array(view_judge))
