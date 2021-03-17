import numpy as np
from sklearn import cluster, datasets, mixture
import datasetPreview as dp

np.random.seed(0)  
n_samples = 1500
no_structure = np.random.rand(n_samples, 2), None
dp.showDataset('preview', no_structure)
