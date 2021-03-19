import numpy as np
import joblib
import sys
sys.path.append("..")
from layer1_vectorize_context import *


class ScatterComments:
    """
    including train and predict models
    """
    def __init__(self, part_cluster=None, role_cluster=None, dr_cluster=None, rs_cluster=None, heatage_cluster=None):
        self.part_cluster = part_cluster
        self.role_cluster = role_cluster
        self.dr_cluster = dr_cluster
        self.rs_cluster = rs_cluster
        self.heatage_cluster = heatage_cluster

        self.part_model = joblib.load('part_model.m')
        self.role_model = joblib.load('role_model.m')
        self.dr_model = joblib.load('dr_model.m')
        self.rs_model = joblib.load('rs_model.m')

    def predict(self, vectorized_context):
        return self._predict_part(self._to_array(vectorized_context[:, 1])), self._predict_role(
            self._to_array(vectorized_context[:, 2])), self._predict_dr(
            self._to_array(vectorized_context[:, 3])), self._predict_rs(
            self._to_array(vectorized_context[:, 4]))\
            # , self._predict_heatage(self._to_array(vectorized_context[:, 5]))

    def _to_array(self, X):
        npa = []
        for v in X:
            npa.append(np.array(v))
        return npa

    def _predict_part(self, y):
        return self.part_model.predict(y)

    def _predict_role(self, y):
        return self.role_model.predict(y)

    def _predict_dr(self, y):
        return self.dr_model.predict(y)

    def _predict_rs(self, y):
        return self.rs_model.predict(y)

    def _predict_heatage(self, y):
        pass


if __name__ == '__main__':
    # aa = ScatterComments()
    # aa.part_model.predict([1,2])
    aa = joblib.load("../part_model.m")
    aa.predict([1, 2])
