#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for k, i in data_dict.items():
    try:
        salary = int(i["salary"])
        if salary > 2.5 * 10 ** 7:
            print k
    except:
        pass
### your code below
# from sklearn.linear_model import LinearRegression
# reg = LinearRegression()
# reg.fit(ages_train, net_worths_train)
#
# print "score: %f" % reg.score(ages_test, net_worths_test)
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


