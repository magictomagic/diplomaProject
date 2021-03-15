import numpy as np
from operator import itemgetter
from layer1_vectorize_context import *
from sklearn.cluster import Birch
from sklearn.cluster import DBSCAN


def cluster_birch(X, n_clusters=None):
    brc = Birch(n_clusters=n_clusters)
    brc.fit(X)
    return brc.predict(X)


def cluster_dbscan(X, n_cluster=3):
    dbs = DBSCAN()
    dbs.fit(X)
    return dbs.fit_predict(X)


if __name__ == '__main__':
    # # 从数据库中读出评论
    # raw_comments = r.hgetall(raw_comments_db)
    #
    # # 使用适当的参数初始化异常检测算法第一层的训练模型
    # pj_module = ProjectComments(6, 8, 4)
    #
    # # 将评论变为可迭代的
    # iter_comment = IterateComments(raw_comments)
    #
    #
    # while True:
    #     misc = iter_comment.iter_loads_comments()
    #     if not isinstance(misc, bool):
    #         c = pj_module.iter_project_quad(*itemgetter(*keys)(misc))
    #         view_judge.append(c)
    #     else:
    #         break
    # print(np.array(view_judge))
    X = np.array([[1, 2], [2, 2], [2, 3],
                  [8, 7], [8, 8], [25, 80]])
    print(cluster_dbscan(X))

