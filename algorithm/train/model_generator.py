from layer2_anomaly_detection import *


class CreateModels:
    def __init__(self, to_train_db):
        self.view_judge = []
        self.raw_comments_to_train = r.hgetall(to_train_db)
        self.vectorize_context = ProjectComments(threshold_role, threshold_dr, threshold_ner)
        self.iter_comment = IterateComments(self.raw_comments_to_train)
        while True:
            misc = self.iter_comment.iter_loads_comments()
            if not isinstance(misc, bool):
                self.view_judge.append(self.vectorize_context.iter_project_quad(*itemgetter(*keys)(misc)))
            else:
                break
        self.to_train = np.array(self.view_judge)
        self.cluster_context = ClusterComments(part_cluster, role_cluster, dr_cluster, rs_cluster, heatage_cluster)
        self.cluster_context.train(self.to_train)

if __name__ == '__main__':
    # print(train_db)
    eyes = CreateModels(train_db)

