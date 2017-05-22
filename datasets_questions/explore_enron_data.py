#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#14
print "Number of features for each person: %d" % len(enron_data.items()[0][1])

#15
poi = 0
for key in enron_data.keys():
    poi += enron_data[key]["poi"]

print "Number of Persons of interest: %d" % poi

#18
print "Total value of stock belonging to James Prentice: %d" % enron_data["PRENTICE JAMES"]["total_stock_value"]

#19
print "Emails from Wesley Colwell to persons of interesets: %d" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#20
print "Number of exercised stock options from Jeffrey K Skilling: %d" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#25
max_total_payments = enron_data["LAY KENNETH L"]["total_payments"]
max_total_payments_person = "LAY KENNETH L"
for person in ("SKILLING JEFFREY K", "FASTOW ANDREW S"):
    if max_total_payments < enron_data[person]["total_payments"]:
        max_total_payments_person = person
        max_total_payments = enron_data[person]["total_payments"]

print "Person with the highest total payment is: %s which errand: %d" % (max_total_payments_person, max_total_payments)