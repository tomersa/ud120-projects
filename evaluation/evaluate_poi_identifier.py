#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

predictions = clf.predict(features_test)

print "POI predicted: %d" % sum(labels_test)
print "people in test set: %d" % sum(1 for i in labels_test)
print "accuracy=%f" % accuracy_score(predictions, labels_test)
print "True positives=%d" % sum(1 if j is True and i is True else 0 for i,j in zip(predictions, labels_test))
print "Precision=%f" % precision_score(predictions, labels_test) 
print "Recall=%f" % precision_score(predictions, labels_test) 

