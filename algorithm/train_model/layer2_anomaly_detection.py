from sklearn.cluster import Birch
import joblib
import sys
sys.path.append("..")
from layer1_vectorize_context import *


class ClusterComments:
    """
    including train and predict models
    """

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
        # ii = 0
        # while ii < 1000:
        #     print("ClusterComments initialize done")
        #     ii += 1

    def train(self, vectorized_context):
        return self._train_part(self._to_array(vectorized_context[:, 1])), self._train_role(
            self._to_array(vectorized_context[:, 2])), self._train_dr(
            self._to_array(vectorized_context[:, 3])), self._train_rs(
            self._to_array(vectorized_context[:, 4])) \
            # , self._train_heatage(self._to_array(vectorized_context[:, 5]))

    # def persistent_storage(self):
    #     jj = 0
    #     while jj < 1000:
    #         jj += 1
    #         print("start persistent storage...")

    def _to_array(self, X):
        npa = []
        for v in X:
            npa.append(np.array(v))
        return npa

    def _train_part(self, X):
        self.part_model = Birch(n_clusters=self.part_cluster)
        self.part_model.fit(X)
        joblib.dump(self.part_model, '../part_model.m')
        # part_model = Birch(n_clusters=self.part_cluster)
        # part_model.fit(X)
        # print("aaaaa")
        # joblib.dump(part_model, 'aapart_model.m')

    def _train_role(self, X):
        self.role_model = Birch(n_clusters=self.role_cluster)
        self.role_model.fit(X)
        joblib.dump(self.role_model, '../role_model.m')

    def _train_dr(self, X):
        self.dr_model = Birch(n_clusters=self.dr_cluster)
        self.dr_model.fit(X)
        joblib.dump(self.dr_model, '../dr_model.m')

    def _train_rs(self, X):
        self.rs_model = Birch(n_clusters=self.rs_cluster)
        self.rs_model.fit(X)
        joblib.dump(self.rs_model, '../rs_model.m')

    def _train_heatage(self, X):
        pass
        # np_X = self.to_array(X)
        # heatage_model = Birch(n_clusters=self.heatage_cluster)
        # heatage_model.fit(np_X)
        # return heatage_model


if __name__ == '__main__':
    part_model = joblib.load("aapart_model.m")
    part_model.predict([1, 2])
