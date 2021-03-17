from pyod.models.cblof import CBLOF  
from pyod.utils.data import generate_data
from pyod.utils.example import visualize

X_train, X_test, y_train, y_test = generate_data(n_train=2000, n_test=1000, n_features=2, behaviour="new")

clf_name = 'CBLOF'
clf = CBLOF()
clf.fit(X_train)

y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
y_train_scores = clf.decision_scores_  # raw outlier scores

y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
y_test_scores = clf.decision_function(X_test)  # outlier scores

visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred, y_test_pred, show_figure=True, save_figure=False)