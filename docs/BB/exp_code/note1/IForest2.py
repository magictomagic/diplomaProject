from pyod.models.iforest import IForest
from pyod.utils.data import generate_data
from pyod.utils.example import visualize, data_visualize

X_train, X_test, y_train, y_test = generate_data(n_train=2000, n_test=1000, n_features=2, behaviour="new")

clf_name = 'PCA'
clf = PCA()
clf.fit(X_train)