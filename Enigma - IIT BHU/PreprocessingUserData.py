#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 07:04:18 2017

@author: gokul

import os
os.chdir('/media/gokul/Academic/!.Events/Code Fest IIT BHU 17/Enigma')
os.getcwd()
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Cleaning user_data.csv
user_data = pd.read_csv('train/user_data.csv')
print(user_data.dtypes)

print(user_data.isnull().any())
user_data['country'].fillna('Unknown', inplace = True)

user_data['rank'].unique()
user_data['rank'].replace({'beginner' : 1, 'intermediate' : 2, 'advanced' : 3, 'expert': 4}, inplace = True)

#Writing cleaned file
user_data.to_csv('train/user_data_cleaned.csv')