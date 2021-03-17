import numpy as np
from sklearn import cluster, datasets, mixture
import datasetPreview as dp

np.random.seed(0)  
n_samples = 1500
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)
dp.showDataset('preview', aniso)
