#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:09:48 2017

@author: gokul
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


prob_data = pd.read_csv('train/problem_data_cleaned.csv')
user_data = pd.read_csv('train/user_data_cleaned.csv')
train_data = pd.read_csv('train/train_submissions.csv')

train_data_new = pd.DataFrame(train_data[['user_id', 'problem_id', 'attempts_range']])

####
#for i in train_data_new['user_id']:
#    print user_data[user_data['user_id'] == i].values[0][2:]
#    print '-'*70
#    
#for i in train_data_new['problem_id']:
#    print prob_data[prob_data['problem_id'] == i].values[0][2:]
#    print '-'*70
#    
#print train_data_new['attempts_range']
#####
# X3_df->features u_series->predictor
X1 = [user_data[user_data['user_id'] == i].values[0][2:] for i in train_data_new['user_id']]
X1_df = pd.DataFrame(X1)
X1_df.columns = list(user_data.columns)[2:]
X1_df.reset_index(inplace = True)
X2 = [prob_data[prob_data['problem_id'] == i].values[0][2:] for i in train_data_new['problem_id']]
X2_df = pd.DataFrame(X2)
X2_df.columns = list(prob_data.columns)[2:]
X2_df.reset_index(inplace = True)

X3_df = pd.DataFrame(X2_df)
for col in X1_df.columns[1:]:
    X3_df[col] = X1_df[col]
del X3_df['index']

y = train_data_new['attempts_range'].values
y_series = pd.Series(y) 

train_data = pd.DataFrame(X3_df)
train_data['attempts_range'] = y_series
train_data.to_csv('train_data.csv', index = False)

#Formatting test data
# X3_df_test->features 
test_data = pd.read_csv('test_submissions.csv')
test_data_new = pd.DataFrame(test_data[['user_id', 'problem_id']])
X1_test = [user_data[user_data['user_id'] == i].values[0][2:] for i in test_data_new['user_id']]
X1_df_test = pd.DataFrame(X1_test)
X1_df_test.columns = list(user_data.columns)[2:]
X1_df_test.reset_index(inplace = True)
X2_test = [prob_data[prob_data['problem_id'] == i].values[0][2:] for i in test_data_new['problem_id']]
X2_df_test = pd.DataFrame(X2_test)
X2_df_test.columns = list(prob_data.columns)[2:]
X2_df_test.reset_index(inplace = True)

X3_df_test = pd.DataFrame(X2_df_test)
for col in X1_df_test.columns[1:]:
    X3_df_test[col] = X1_df_test[col]
del X3_df_test['index']

test_data = pd.DataFrame(X3_df_test)
test_data.to_csv('test_data.csv', index = False)