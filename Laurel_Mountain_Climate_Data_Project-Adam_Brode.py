#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:33:04 2021

@author: brodeam
"""


import csv

with open('C:\\Users\\brode\\Python\\Laurel Mountain Historical Climate Data\\LaurelMountainTempsFebruary1971.csv') as tempfile:
    
    rec_count = 0
    
    days_over = 0
    
    days_under = 0
 
    temp_reader = csv.DictReader(tempfile, delimiter =',', quotechar='\"') 
                                
    for temp_record in temp_reader:
        
        rec_count += 1
    
        if temp_record['Maximum'].isnumeric():
          
            daily_max = temp_record['Maximum']
          
            daily_max = int(daily_max)
            
        if daily_max > 32:
            
            days_over += 1
            
        else:
            
            days_under += 1
            
            
print("days over 32 in December 1970: ", days_over)
print("days under 32 in December 1970: ", days_under)
        
#Need to seriously rethink the viability of this whole project.  Cleaning up this data will take an eternity.  Just work with UN data?  UN Climate Data?