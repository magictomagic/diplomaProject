from pyod.models.abod import ABOD
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print
from pyod.utils.example import visualize

X_train, X_test, y_train, y_test = generate_data(n_train=200, n_test=100, n_features=2)
clf = ABOD(method="fast") # initialize detector
clf.fit(X_train) # Fit detector

y_test_pred = clf.fit(X_test) # binary labels
y_test_scores = clf.decision_function(X_test) # raw outlier scores
y_test_proba = clf.predict_proba(X_test) # outlier probability # predict_proba

evaluate_print("ABOD", y_test, y_test_scores) # performance evaluation

# visualize(y_test, y_test_scores) # prediction visualization
visualize(X_train, y_train, X_test, y_test, y_train_pred, y_test_pred, show_figure=True, save_figure=False)

# 换个字体：这个项目的源码迭代比较快，文档跟不上，我是读了它的源码，包括如何生成随机的数据，如何...，后再调用它的方法的。