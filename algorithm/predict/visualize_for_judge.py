import pandas as pd
from layer2_anomaly_detection import *


class Visualization:
    def __init__(self, to_train_db, to_predict_db):
        self.view_judge = []
        self.raw_comments_to_train = r.hgetall(to_train_db)
        self.raw_comments_to_predict = r.hgetall(to_predict_db)
        self.vectorize_context = ProjectComments(6, 8, 4)  # 这里可以调参
        self.iter_comment = IterateComments(self.raw_comments_to_train)
        while True:
            misc = self.iter_comment.iter_loads_comments()
            if not isinstance(misc, bool):
                c = self.vectorize_context.iter_project_quad(*itemgetter(*keys)(misc))
                self.view_judge.append(c)
            else:
                break
        self.to_train = np.array(self.view_judge)
        self.to_predict = self.to_train  # 暂时先这样搞
        self.cluster_context = ClusterComments()  # 这里也可以调参
        self.show_predict = None

    def to_train_predict(self):
        self.cluster_context.train(self.to_train)
        predicted = self.cluster_context.predict(self.to_predict)
        self.show_predict = list(predicted)
        self.show_predict.append(self.to_predict[:, 0])
        return self.show_predict

    def save_to_csv(self):
        data_chunk = self.to_train_predict()
        cont_list = []
        data_scale = len(data_chunk[0])
        index = 0
        while index < data_scale:
            data_slice = np.array(data_chunk)[:, index]
            cont_list.append({"part": data_slice[0],
                              "role": data_slice[1],
                              "dr": data_slice[2],
                              "rs": data_slice[3],
                              "comment_texts": data_slice[4]})
            index += 1
        df = pd.DataFrame(cont_list, columns=["comment_texts", "role", "dr", "rs", "part"])
        # print(df)
        df.to_csv("./look1.csv", index=False, encoding='utf-8')


if __name__ == '__main__':
    eyes = Visualization("comments_zh", "comments_zh")
    eyes.save_to_csv()

