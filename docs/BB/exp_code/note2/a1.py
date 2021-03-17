# https://blog.csdn.net/weixin_41697507/article/details/89408236
from pyod.models.iforest import IForest  
from pyod.models.abod import ABOD
from pyod.models.lof import LOF
from pyod.models.cblof import CBLOF
from pyod.models.iforest import IForest 
from pyod.models.pca import PCA 
from pyod.models.ocsvm import OCSVM

from pyod.utils.data import generate_data, get_outliers_inliers
from pyod.utils.example import visualize
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.font_manager

data_size = 300

X_train, Y_train = generate_data(n_train=data_size, train_only=True, n_features=2, behaviour="new")

# by default the outlier fraction is 0.1 in generate data function 
outlier_fraction = 0.1

# store outliers and inliers in different numpy arrays
x_outliers, x_inliers = get_outliers_inliers(X_train,Y_train)

n_inliers = len(x_inliers)
n_outliers = len(x_outliers)

#separate the two features and use it to plot the data 
F1 = X_train[:,[0]].reshape(-1,1)
F2 = X_train[:,[1]].reshape(-1,1)

xx , yy = np.meshgrid(np.linspace(-10, 10, data_size), np.linspace(-10, 10, data_size))

# scatter plot 
plt.scatter(F1,F2)
plt.xlabel('F1')
plt.ylabel('F2') 

classifiers = {
     #'Angle-based Outlier Detector (ABOD)' : ABOD(contamination=outlier_fraction),
     'k-means clustering' : CBLOF(contamination=outlier_fraction),
     'Isolation forest': IForest(contamination=outlier_fraction),
     'Local Outlier Factor' : LOF(contamination=outlier_fraction),
     'Principal component analysis' : PCA(contamination=outlier_fraction),
     'One Class Support Vector Machine' : OCSVM(contamination=outlier_fraction)
}

class_nums = len(classifiers)

#set the figure size
plt.figure(figsize=(10, 10))

for i, (clf_name,clf) in enumerate(classifiers.items()) :
    # fit the dataset to the model
    clf.fit(X_train)

    # predict raw anomaly score
    scores_pred = clf.decision_function(X_train)*-1

    # prediction of a datapoint category outlier or inlier
    y_pred = clf.predict(X_train)
    n_inliers = len(y_pred) - np.count_nonzero(y_pred)
    n_outliers = np.count_nonzero(y_pred == 1)

    # no of errors in prediction
    # n_errors = (y_pred != Y_train).sum()
    # print('No of Errors : ',clf_name, n_errors)
    print('Algorithm: ', clf_name, '    OUTLIERS: ', n_outliers, '  INLIERS: ',n_inliers)
    # rest of the code is to create the visualization

    # threshold value to consider a datapoint inlier or outlier
    threshold = stats.scoreatpercentile(scores_pred,100 *outlier_fraction)

    # decision function calculates the raw anomaly score for every point
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]) * -1
    Z = Z.reshape(xx.shape)

    subplot = plt.subplot(1, class_nums, i + 1)

    # fill blue colormap from minimum anomaly score to threshold value
    subplot.contourf(xx, yy, Z, levels = np.linspace(Z.min(), threshold, 10),cmap=plt.cm.Blues_r)

    # draw red contour line where anomaly score is equal to threshold
    a = subplot.contour(xx, yy, Z, levels=[threshold],linewidths=2, colors='red')

    # fill orange contour lines where range of anomaly score is from threshold to maximum anomaly score
    subplot.contourf(xx, yy, Z, levels=[threshold, Z.max()],colors='orange')

    # scatter plot of inliers with white dots
    b = subplot.scatter(X_train[:-n_outliers, 0], X_train[:-n_outliers, 1], c='white',s=20, edgecolor='k') 
    # scatter plot of outliers with black dots
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