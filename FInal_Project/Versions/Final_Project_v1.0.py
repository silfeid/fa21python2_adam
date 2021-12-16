# -*- coding: utf-8 -*-
"""
Created on Fri December 10 20:55:41 2021

@author: Adam Brode (brodeam@gmail.com) 
"""
import csv
import json
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

directory = 'fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Snowdays_Only/Test/'

df_dict = {}

for filename in os.listdir(directory):

    if filename.endswith('.csv'):
        filename = filename.replace('.csv', '')
        df_dict[filename] = pd.read_csv(directory+filename+'.csv')
        df_dict[filename] = df_dict[filename].set_index('ObDate')

for dongle in df_dict:
    print(dongle)
    print(df_dict[dongle])