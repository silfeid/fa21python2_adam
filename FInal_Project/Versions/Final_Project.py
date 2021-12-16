# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:57:50 2021

@author: brode
"""
import csv
import json
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

directory = 'fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Snowdays_Only/'

#Need to make a dictionary; keys are filenames, values are dataframes (can be done)

df_dict = {}

for filename in os.listdir(directory):

    if filename.endswith('.csv'):
        filename = filename.replace('.csv', '')
        df_dict[filename] = pd.read_csv(directory+filename+'.csv')

print(df_dict['Dubois_Snow'])