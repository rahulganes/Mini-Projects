#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:01:24 2017

@author: gokul

import os
os.chdir('/media/gokul/Academic/!.Events/Code Fest IIT BHU 17/Enigma')
os.getcwd()
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Cleaning problem_data.csv
prob_data = pd.read_csv('train/problem_data.csv')
print(prob_data.dtypes)

#changing level_type to numeric
difficulty_points = {chr(i) : i-ord('A')+1 for i in range(ord('A'), ord('N')+1)}
prob_data['level_type'].replace(difficulty_points, inplace = True)
prob_data['level_type'].fillna(int(prob_data['level_type'].mean()), inplace = True)

#Imputing missing data in points
points = dict(prob_data.groupby('level_type')['points'].mean())
plt.plot(points.keys(), points.values())
plt.show()

X = np.array([points.keys()[:8]])
y = np.array(points.values()[:8])
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X.reshape(-1, 1), y)

pred_points = {i:int(regressor.predict(i)) for i in range(1, 15)}

for i in range(len(prob_data)):
    if pd.isnull(prob_data['points'][i]):
        prob_data.loc[i,'points'] = pred_points[prob_data['level_type'][i]]
        
#Buiding new columns of problem domain
prob_data['tags'].fillna('unclasssified', inplace = True)
tag_list = []
for items in prob_data['tags']:
    for item in items.split(','):
        if item not in tag_list:
            tag_list.append(item)

print(tag_list)

for tag in tag_list:
    prob_data[tag] = map(lambda x: int(tag in x), prob_data.loc[:,'tags'])
    
#Removing tags column
del prob_data['tags']

#Writing cleaned file
prob_data.to_csv('train/problem_data_cleaned.csv')