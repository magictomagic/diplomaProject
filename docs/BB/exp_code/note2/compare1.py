from pyod.utils.data import generate_data, get_outliers_inliers
from pyod.utils.example import visualize
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager

from pyod.models.iforest import IForest  
from pyod.models.abod import ABOD
from pyod.models.lof import LOF
from pyod.models.cblof import CBLOF
from pyod.models.iforest import IForest 
from pyod.models.pca import PCA 
from pyod.models.ocsvm import OCSVM

data_size = 300
outlier_fraction = 0.1

X_train, Y_train = generate_data(n_train=data_size, train_only=True, n_features=2, behaviour="new")
x_outliers, x_inliers = get_outliers_inliers(X_train,Y_train)
n_inliers = len(x_inliers)
n_outliers = len(x_outliers)
F1 = X_train[:,[0]].reshape(-1,1)
F2 = X_train[:,[1]].reshape(-1,1)
xx , yy = np.meshgrid(np.linspace(-10, 10, data_size), np.linspace(-10, 10, data_size))
plt.scatter(F1,F2)
plt.xlabel('F1')
plt.ylabel('F2') 

classifiers = {
     'k-means clustering' : CBLOF(contamination=outlier_fraction),
     'Isolation forest': IForest(contamination=outlier_fraction),
     'Local Outlier Factor' : LOF(contamination=outlier_fraction),
     'Principal component analysis' : PCA(contamination=outlier_fraction),
     'One Class Support Vector Machine' : OCSVM(contamination=outlier_fraction)
}

class_nums = len(classifiers)
plt.figure(figsize=(10, 10))

for i, (clf_name,clf) in enumerate(classifiers.items()) :
    clf.fit(X_train)

    # predict raw anomaly score
    scores_pred = clf.decision_function(X_train)*-1

    # prediction of a datapoint category outlier or inlier
    y_pred = clf.predict(X_train)

    n_inliers = len(y_pred) - np.count_nonzero(y_pred)
    n_outliers = np.count_nonzero(y_pred == 1)

    print('Algorithm: ', clf_name, '    OUTLIERS: ', n_outliers, '  INLIERS: ',n_inliers)

    # visualize
    threshold = stats.scoreatpercentile(scores_pred,100 *outlier_fraction)
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]) * -1
    Z = Z.reshape(xx.shape)
    subplot = plt.subplot(1, class_nums, i + 1)
    subplot.contourf(xx, yy, Z, levels = np.linspace(Z.min(), threshold, 10),cmap=plt.cm.Blues_r)
    a = subplot.contour(xx, yy, Z, levels=[threshold],linewidths=2, colors='red')
    subplot.contourf(xx, yy, Z, levels=[threshold, Z.max()],colors='orange')
    b = subplot.scatter(X_train[:-n_outliers, 0], X_train[:-n_outliers, 1], c='white',s=20, edgecolor='k') 
    c = subplot.scatter(X_train[-n_outliers:, 0], X_train[-n_outliers:, 1], c='black',s=20, edgecolor='k')
    subplot.axis('tight')
    subplot.legend(
        [a.collections[0], b, c],
        ['learned decision function', 'true inliers', 'true outliers'],
        prop=matplotlib.font_manager.FontProperties(size=10),
        loc='lower right')
    subplot.set_title(clf_name)
    subplot.set_xlim((-10, 10))
    subplot.set_ylim((-10, 10))
plt.show() 