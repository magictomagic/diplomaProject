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
        self.raw_comments_to_predict = r.hgetall(to_predict_db)
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
        print(self.predicted)
        print(self.id_judge)
        print(jl)
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
        df.to_csv("../look1.csv", index=False, encoding='utf-8')

    def strategy(self):
        """
        过滤链
        :return: {id_judge: flag_killer}
        """
        pass

    def role(self):
        """
        第一层过滤：等级分为 1 - 6，1 表示确定是要的，6 表示确定不要
        :return:
        """
        role_v = self.predicted[1]
        index = 0
        for group in role_v:
            self.flag_killer[index] = role_delete.get(group, 8964)
            index += 1
        print(self.flag_killer)

    def dr(self):
        pass

    def rs(self):
        pass

    def part(self):
        pass

    # def end(self):
    #     """
    #     需要拿到评论的ID，在这里可以只传flag_killer，到父级再组合（只要确保是继承自同一块内存中的字符串即可）
    #     :return: {"id|id|id": flag_i, ...}
    #     """


if __name__ == '__main__':
    # print(role_delete.get(2, 100))
    eyes = CommentsFilter(predict_db, output=False)
    eyes.role()

