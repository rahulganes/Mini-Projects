# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:18:36 2018

@author: new
"""

#%% 0
'''
Set the working directory
'''
import os
os.chdir('D:\!.Events\Vortex 18\Dataset_ml')

#%% 1
'''
Import the necessary packages
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#%% 2
'''
Read the data files
'''
train = pd.read_csv('train_ml.csv',  index_col=0)
test = pd.read_csv('test_ml.csv',  index_col=0)

test['loan_status'] = -1
dataset = pd.concat([train, test])

#%% 3
'''
Explore the train and test data
'''
print(train.info())
print(train.describe())

print(test.info())

#%% 4
'''
Clean the data frame columns
'''

dataset['term'] = dataset['term'].str.extract('(\d+)').astype(int)

dataset['grade'].value_counts()
dataset['grade'] = pd.Categorical(dataset['grade'], ordered=True,
       categories=['A', 'B', 'C', 'D', 'E', 'F','G'] )
dataset = dataset.drop('grade', axis=1)

dataset['sub_grade'].value_counts()
dataset['sub_grade'] = pd.Categorical(dataset['sub_grade'], ordered=True,
       categories=['A1','A2', 'A3','A4','A5',
                   'B1','B2', 'B3','B4','B5',
                   'C1','C2', 'C3','C4','C5',
                   'D1','D2', 'D3','D4','D5',
                   'E1','E2', 'E3','E4','E5',
                   'F1','F2', 'F3','F4','F5',
                   'G1','G2', 'G3','G4','G5'])
sub_grade_dict = dict(enumerate(dataset['sub_grade'].cat.categories))
dataset['sub_grade'] = dataset['sub_grade'].cat.codes

dataset = dataset.drop('emp_title', axis=1)

dataset['pymnt_plan'].unique()
dataset['pymnt_plan'] = dataset['pymnt_plan'].map({'n':0, 'y':1})

dataset = dataset.drop('desc', axis=1)

dataset['zip_code'] = dataset['zip_code'].str.extract('(\d+)').astype(int)

dataset['initial_list_status'].value_counts()
dataset['initial_list_status'] = dataset['initial_list_status'].map({'f':0, 'w':1})

dataset['application_type'].value_counts()
dataset['application_type'] = dataset['application_type'].map({'INDIVIDUAL':0, 'JOINT':1})

dataset.loc[dataset['last_week_pay']=='NAth week','last_week_pay'] = '0th week'
dataset['last_week_pay'] = dataset['last_week_pay'].str.extract('(\d+)').astype(int)

#%% 5
'''
One hot encoding
'''
# Encoding categorical data
# Encoding the Independent Variable

char_cols = ['batch_enrolled', 'emp_length', 'home_ownership', 'verification_status', 'purpose',
              'addr_state', 'verification_status_joint']

for c in char_cols:
    one_hot_df = pd.get_dummies(dataset.loc[:,c])
    one_hot_df.columns = [str(c)+"_"+x for x in one_hot_df.columns]
    dataset = dataset.drop(c, axis=1)
    dataset = dataset.join(one_hot_df)

dataset = dataset.drop('title', axis=1)

#%% 6
'''
Splitting into train and test dataset
'''
train = dataset.iloc[:425903,]

# Move the loan_status to last
col_names = list(train.columns)
col_names.remove("loan_status")
col_names.append("loan_status")
train = train[col_names]

test = dataset.iloc[425903:,]
#Drop the dependant column
test = test.drop("loan_status", axis=1)

#%% 7
'''
Building the model
'''
X = train.iloc[:,:-1].fillna(0)
y = train.iloc[:,-1]

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 25, random_state = 0)
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(test.fillna(0))

result = pd.DataFrame({'member_id':test.index, "loan_status":y_pred})
result = result[result.columns[::-1]]
result.to_csv("result_banking_n25.csv", index=False)
