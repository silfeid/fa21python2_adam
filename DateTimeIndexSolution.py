# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:10:15 2021

@author: brode"""

import csv
import json
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import numpy as np


index = pd.date_range(start = "1970-01-01", end = "2013-12-31", freq = "Y")
index = [pd.to_datetime(date, format='%Y-%m-%d').date() for date in index]
data = np.random.randint(1,100, size=len(index))
df = pd.DataFrame(data=data,index=index, columns=['data'])
print (df.head())
    
plt.plot(df)