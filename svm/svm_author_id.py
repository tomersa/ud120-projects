#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svm = SVC(kernel='linear', C=1)

#########################################################
t0 = time()
svm.fit(features_train, labels_train)
print "training time fit():", round(time()-t0, 3), "s"

t0 = time()
results_test = svm.predict(features_test)
print "training time predict():", round(time()-t0, 3), "s"

accuracy = accuracy_score(labels_test, results_test)
print "for %d labels in test, svm recieved an accuracy of: %f" % (len(labels_test), accuracy)
#########################################################
