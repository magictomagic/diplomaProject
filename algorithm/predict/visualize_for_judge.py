import pandas as pd
from layer2_anomaly_detection import *


class Visualization:
    def __init__(self, to_predict_db):
        self.view_judge = []
        self.raw_comments_to_predict = r.hgetall(to_predict_db)
        self.vectorize_context = ProjectComments(6, 8, 4)  # 这里可以调参
        self.iter_comment = IterateComments(self.raw_comments_to_predict)
        while True:
            misc = self.iter_comment.iter_loads_comments()
            if not isinstance(misc, bool):
                self.view_judge.append(self.vectorize_context.iter_project_quad(*itemgetter(*keys)(misc)))
            else:
                break
        self.to_predict = np.array(self.view_judge)
        self.cluster_context = ScatterComments()  # 这里也可以调参
        predicted = self.cluster_context.predict(self.to_predict)
        self.show_predict = list(predicted)
        self.show_predict.append(self.to_predict[:, 0])
        self.data_chunk = self.show_predict


    def save_to_csv(self):
        cont_list = []
        data_scale = len(self.data_chunk[0])
        index = 0
        while index < data_scale:
            data_slice = np.array(self.data_chunk)[:, index]
            cont_list.append({"part": data_slice[0],
                              "role": data_slice[1],
                              "dr": data_slice[2],
                              "rs": data_slice[3],
                              "comment_texts": data_slice[4]})
            index += 1
        df = pd.DataFrame(cont_list, columns=["comment_texts", "role", "dr", "rs", "part"])
        df.to_csv("../look1.csv", index=False, encoding='utf-8')


if __name__ == '__main__':
    eyes = Visualization(predict_db)
    eyes.save_to_csv()

