from pyod.models.lof import LOF  
from pyod.utils.data import generate_data
from pyod.utils.example import visualize

X_train, X_test, y_train, y_test = generate_data(n_train=2000, n_test=1000, n_features=2, behaviour="new")

clf_name = 'LOF'
clf = LOF()
clf.fit(X_train)

y_train_pred = clf.labels_ 
y_train_scores = clf.decision_scores_
y_test_pred = clf.predict(X_test) 
y_test_scores = clf.decision_function(X_test) 

visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred, y_test_pred, show_figure=True, save_figure=False)