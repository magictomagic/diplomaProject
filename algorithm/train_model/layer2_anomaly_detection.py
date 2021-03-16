import numpy as np
from operator import itemgetter
from layer1_vectorize_context import *
from sklearn.cluster import Birch
from sklearn.cluster import DBSCAN


def cluster_birch(X, n_clusters=None):
    brc = Birch(n_clusters=n_clusters)
    brc.fit(X)
    return brc.fit_predict([[0.2, 1], [0.2, -1]])
    # return brc.predict(X)


def cluster_train_model(cluster_algorithm, X, n_clusters=None):
    train = cluster_algorithm(n_clusters=n_clusters)
    train.fit(X)
    return train


class ClusterComments:
    def __init__(self, part_cluster=None, role_cluster=None, dr_cluster=None, rs_cluster=None, heatage_cluster=None):
        self.part_cluster = part_cluster
        self.role_cluster = role_cluster
        self.dr_cluster = dr_cluster
        self.rs_cluster = rs_cluster
        self.heatage_cluster = heatage_cluster

        self.part_model = None
        self.role_model = None
        self.dr_model = None
        self.rs_model = None

    def train(self, vectorized_context):
        return self.train_part(self.to_array(vectorized_context[:, 1])), self.train_role(
            self.to_array(vectorized_context[:, 2])), self.train_dr(
            self.to_array(vectorized_context[:, 3])), self.train_rs(
            self.to_array(vectorized_context[:, 4])), self.train_heatage(
            self.to_array(vectorized_context[:, 5]))

    def predict(self, vectorized_context):
        return self.predict_part(self.to_array(vectorized_context[:, 1])), self.predict_role(
            self.to_array(vectorized_context[:, 2])), self.predict_dr(
            self.to_array(vectorized_context[:, 3])), self.predict_rs(
            self.to_array(vectorized_context[:, 4])), self.predict_heatage(
            self.to_array(vectorized_context[:, 5]))

    def to_array(self, X):
        npa = []
        for v in X:
            npa.append(np.array(v))
        return npa

    def train_part(self, X):
        # np_X = self.to_array(X)
        self.part_model = Birch(n_clusters=self.part_cluster)
        self.part_model.fit(X)
        # return part_model

    def train_role(self, X):
        # np_X = self.to_array(X)
        self.role_model = Birch(n_clusters=self.role_cluster)
        self.role_model.fit(X)
        # return role_model

    def train_dr(self, X):
        # np_X = self.to_array(X)
        self.dr_model = Birch(n_clusters=self.dr_cluster)
        self.dr_model.fit(X)
        # return dr_model

    def train_rs(self, X):
        # np_X = self.to_array(X)
        self.rs_model = Birch(n_clusters=self.rs_cluster)
        self.rs_model.fit(X)
        # return rs_model

    def train_heatage(self, X):
        pass
        # np_X = self.to_array(X)
        # heatage_model = Birch(n_clusters=self.heatage_cluster)
        # heatage_model.fit(np_X)
        # return heatage_model

    def predict_part(self, y):
        return self.part_model.predict(y)

    def predict_role(self, y):
        return self.role_model.predict(y)

    def predict_dr(self, y):
        return self.dr_model.predict(y)

    def predict_rs(self, y):
        return self.rs_model.predict(y)

    def predict_heatage(self, y):
        pass


if __name__ == '__main__':
    raw_comments = r.hgetall(raw_comments_db)
    vectorize_context = ProjectComments(6, 8, 4)
    iter_comment = IterateComments(raw_comments)

    while True:
        misc = iter_comment.iter_loads_comments()
        if not isinstance(misc, bool):
            c = vectorize_context.iter_project_quad(*itemgetter(*keys)(misc))
            view_judge.append(c)
        else:
            break

    to_be_trained = np.array(view_judge)
    # print(to_be_trained)
    cluster_context = ClusterComments()
    cluster_context.train(to_be_trained)
    # cluster_context.predict()
    print(cluster_context.predict(to_be_trained))

    # print(np.array(view_judge))
