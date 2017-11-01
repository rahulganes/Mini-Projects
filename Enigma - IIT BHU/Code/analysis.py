#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 07:24:49 2017

@author: gokul

import os
os.chdir('/media/gokul/Academic/!.Events/Code Fest IIT BHU 17/Enigma')
os.getcwd()
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')
X_train = train_data.loc[:, train_data.columns != 'attempts_range']
y_train = train_data['attempts_range']
X_test = test_data[:]
test_ID = pd.read_csv('test_submissions.csv')['ID']


#Coverting country to sparse
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()

lb_results_train  = lb.fit_transform(X_train.loc[:, 'country'] )
X_train2 = pd.concat([X_train, pd.DataFrame(lb_results_train, columns=lb.classes_)], axis=1)
X_train2 = X_train2.drop('country',axis=1)

lb_results_test  = lb.transform(X_test.loc[:, 'country'] )
X_test2 = pd.concat([X_test, pd.DataFrame(lb_results_test, columns=lb.classes_)], axis=1)
X_test2 = X_test2.drop('country',axis=1)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# Feature Scaling 1 : scaling without 'country'
X_train_scaled = sc.fit_transform(X_train.loc[:, X_train.columns != 'country'])
X_test_scaled = sc.transform(X_test.loc[:, X_test.columns != 'country'])

# Feature Scaling 2 : scaling with 'country'
X_train2_scaled = sc.fit_transform(X_train2.loc[:])
X_test2_scaled = sc.transform(X_test2.loc[:])

#Witoud scaling
X_train3 = X_train.loc[:, X_train.columns != 'country'] 
X_test3 = X_test.loc[:, X_test.columns != 'country'] 


#writing file
#pd.DataFrame(X_train_scaled).to_csv('train_data_scaled.csv')
#pd.DataFrame(X_test_scaled).to_csv('test_data_scaled.csv')
#
##Reading files
#X_train_scaled = pd.read_csv('train_data_scaled.csv')
#X_test_scaled = pd.read_csv('test_data_scaled.csv')
#y_train = pd.read_csv('train_data.csv')['attempts_range']
#test_ID = pd.read_csv('test_submissions.csv')['ID']

# 1.1 Random Forests- (BEST) with 50 e and r0; without country
# Fitting Random Forest Classification; Attributes : Except country; Scaled: yes
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state =0, n_jobs=-1)
classifier.fit(X_train2_scaled, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test2_scaled)


#Creating the output file
output = pd.DataFrame(test_ID)
output['attempts_range'] = y_pred
output.to_csv('test_predictions.csv')


