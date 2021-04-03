# import os
# import sys
# sys.path.append(os.getcwd())
import pandas as pd
from algorithm.predict.layer2_anomaly_detection import *


class Visualization:
    def __init__(self, to_predict_db):
        comments_filter = CommentsFilter(to_predict_db)
        self.predicted = comments_filter.predicted

    def save_to_csv(self):
        cont_list = []
        data_scale = len(self.predicted[0])
        index = 0
        while index < data_scale:
            data_slice = np.array(self.predicted)[:, index]
            cont_list.append({"part": data_slice[0],
                              "role": data_slice[1],
                              "dr": data_slice[2],
                              "rs": data_slice[3],
                              "comment_texts": data_slice[4]})
            index += 1
        df = pd.DataFrame(cont_list, columns=["comment_texts", "role", "dr", "rs", "part"])
        df.to_csv("../look1.csv", index=False, encoding='utf-8')


class CommentsFilter:
    def __init__(self, to_predict_db, output=False):
        """
        初始化所有是否过滤的 flag 为 0
        :param to_predict_db:
        """
        self.view_judge = []
        self.id_judge = []

        # TODO: replace "to_predict_db" into from string
        self.raw_comments_to_predict = r.hgetall(to_predict_db)
        # with open('input_format.txt', 'w+', encoding='utf8') as f:
        #     f.write(str(self.raw_comments_to_predict))

        self.vectorize_context = ProjectComments(threshold_role, threshold_dr, threshold_ner)
        self.iter_comment = IterateComments(self.raw_comments_to_predict)
        while True:
            misc = self.iter_comment.iter_loads_comments()
            if not isinstance(misc, bool):
                self.view_judge.append(self.vectorize_context.iter_project_quad(*itemgetter(*keys)(misc)))
                self.id_judge.append(misc['hash_id'])
            else:
                break
        self.to_predict = np.array(self.view_judge)
        self.cluster_context = ScatterComments(part_cluster, role_cluster, dr_cluster, rs_cluster, heatage_cluster)
        self.predicted = list(self.cluster_context.predict(self.to_predict))
        self.predicted.append(self.to_predict[:, 0])
        jl = len(self.id_judge)
        if jl < 3:
            print("发生甚么事了？")
        self.flag_killer = [0] * jl
        # print(self.predicted)
        # print(self.id_judge)
        # print(jl)
        # self.predicted
        output and self.save_to_csv()

    def save_to_csv(self):
        cont_list = []
        data_scale = len(self.predicted[0])
        index = 0
        while index < data_scale:
            data_slice = np.array(self.predicted)[:, index]
            cont_list.append({"part": data_slice[0],
                              "role": data_slice[1],
                              "dr": data_slice[2],
                              "rs": data_slice[3],
                              "comment_texts": data_slice[4]})
            index += 1
        df = pd.DataFrame(cont_list, columns=["comment_texts", "role", "dr", "rs", "part"])
        df.to_csv("label.csv", index=False, encoding='utf-8')

    def to_feel_layer(self, layer=3):
        """
        输入几就看第几层
        """
        self.strategy(layer)
        cont_list = []
        data_scale = len(self.predicted[0])
        index = 0
        which_layer = "filter_{}".format(layer)
        while index < data_scale:
            data_slice = np.array(self.predicted)[:, index]
            cont_list.append({"part": data_slice[0],
                              "role": data_slice[1],
                              "dr": data_slice[2],
                              "rs": data_slice[3],
                              which_layer: self.flag_killer[index],
                              "comment_texts": data_slice[4]})
            index += 1
        df = pd.DataFrame(cont_list, columns=["comment_texts", which_layer, "part", "role", "dr", "rs"])
        # print(df)
        # print(self.predicted)
        df.to_csv("feel_{}.csv".format(layer), index=False, encoding='utf-8')

    def strategy(self, layer):
        """
        过滤链
        :return: {id_judge: flag_killer}
        """
        if layer > 1:
            self.role()
        if layer > 2:
            self.dr()
        if layer > 3:
            self.part()
        if layer > 4:
            self.rs()

    def persist_storage(self):
        self.strategy(5)
        # TODO: store to redis in hashmap, only use first field in flag_killer
        print(self.id_judge)
        print(self.flag_killer)

    def role(self):
        """
        第一层过滤：等级分为 1 - 6，1 是默认值，表示确定是要的，6 表示确定不要
        :return:
        """
        print("start role filter")
        role_v = self.predicted[1]
        index = 0
        for group in role_v:
            self.flag_killer[index] = role_delete.get(group, 1)
            index += 1
        # print(self.flag_killer)

    def dr(self):
        """
        第二层过滤：分的类粒度更细，接收上一层的残渣
        对第一层设置过滤等级，推荐3,4,5,6，我的幸运数字。这里我用5, 就是说5,6都不要
        然后自身再通过 感觉算法 来调参，使过滤更加精确
        1，2，3，4进行分
        """
        print("start dr filter")
        dr_v = self.predicted[2]
        index = 0
        for group in dr_v:
            if self.flag_killer[index] < 5:
                self.flag_killer[index] = dr_delete.get(group, 1)
            index += 1
        # print(self.flag_killer)

    def rs(self):
        """
        所谓物极必反，粒度过于粗应该 留着过年
        """
        print("start rs filter")

    def part(self):
        """
        这边的粒度更加细了，直接感觉不管用了，要先把之前过滤的东西预测一下再感觉
        """
        print("start part filter")
        dr_p = self.predicted[0]
        index = 0
        for group in dr_p:
            if self.flag_killer[index] < 5:
                self.flag_killer[index] = part_delete.get(group, 1)
            index += 1

    # def end(self):
    #     """
    #     需要拿到评论的ID，在这里可以只传flag_killer，到父级再组合（只要确保是继承自同一块内存中的字符串即可）
    #     :return: {"id|id|id": flag_i, ...}
    #     """


if __name__ == '__main__':
    # print(role_delete.get(2, 100))
    eyes = CommentsFilter(predict_db, output=False)
    eyes.role()
