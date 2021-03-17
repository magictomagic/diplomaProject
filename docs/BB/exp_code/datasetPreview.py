import numpy as np, matplotlib.pyplot as mp
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

def showDataset(name, dataset):
    X, y = dataset

    # if y == None:
    #     y = [0] * X.shape[0]

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


if __name__ == '__main__':
 pass