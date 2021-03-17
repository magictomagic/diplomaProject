from time import time
import numpy as np, matplotlib.pyplot as mp

from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler  # 数据标准化
from itertools import cycle, islice

def showDataset(name, dataset):
    X, y = dataset

    # 去除均值和按单位方差来标准化特征样本数据 X
    X = StandardScaler().fit_transform(X)
    
    mp.title(name, size=10)
    colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                            '#f781bf', '#a65628', '#984ea3',
                                            '#999999', '#e41a1c', '#dede00']),
                                    int(max(y) + 1))))
    colors = np.append(colors, ["#000000"])  # 离群点（若有的话）设为黑色
    mp.scatter(X[:, 0], X[:, 1], s=10, color=colors[y])

    mp.xlim(-2.5, 2.5)
    mp.ylim(-2.5, 2.5)
    mp.xticks(())
    mp.yticks(())
    mp.show()


"""生成随机样本集"""
# 固定随机种子
np.random.seed(0)  

# 随机样本的数量
n_samples = 1500

# 使用 datasets 生成各种各样的图像
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)

# 返回的数据结构是 tuple(有序，不可变) 形式的：
"""
(
    array([xx, xx], [xx, xx], ... , [xx, xx]),  // 数据
    array(0|1, 0|1, ... , 0|1)                  // 数据对应标签，用于评价而不是训练
)
"""

birch = cluster.Birch(n_clusters=3)
showDataset('birch', noisy_circles)
