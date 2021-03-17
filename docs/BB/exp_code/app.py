import numpy as np
from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
import datasetPreview as dp

if __name__ == '__main__':
    """
    生成随机样本集，返回的数据结构是 tuple(有序，不可变) 形式的：
    (
        array([xx, xx], [xx, xx], ... , [xx, xx]),  // 数据
        array(0|1, 0|1, ... , 0|1)                  // 数据对应标签，用于评价而不是训练
    )
    """
    np.random.seed(0)  
    n_samples = 1500
    noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)

    dp.showDataset('preview', datasets.make_checkerboard())
