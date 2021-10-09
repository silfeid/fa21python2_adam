# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:57:50 2021

@author: brode
"""
import csv
import json
import os.path

directory = r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\1970s'
    
query_results = {}

def monthly_temp_max_reader():
    
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_max_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_max_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_max_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_max_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)
                        
def monthly_temp_min_reader():
    
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[2] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_min_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_min_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_min_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_min_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)
                        
def monthly_snowdepth_reader():
    
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[-1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\snowdepth_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\snowdepth_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\snowdepth_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\snowdepth_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)

def search_function(query_results):

    quit_commands = ['Q', 'q']
    cum_max = 0
    cum_max_rec_days = 0
    cum_max_miss_days = 0
    cum_min = 0
    cum_min_rec_days = 0
    cum_min_miss_days = 0
    cum_snowdepth = 0
    cum_snow_rec_days = 0
    cum_snow_miss_days = 0

    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_max_data.json') as temp_max_dict_object:
        temp_max_dict = temp_max_dict_object.read()
        temp_max_dict_object.close()
        temp_max_dict = json.loads(temp_max_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_min_data.json') as temp_min_dict_object:
        temp_min_dict = temp_min_dict_object.read()
        temp_min_dict_object.close()
        temp_min_dict = json.loads(temp_min_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\snowdepth_data.json') as snowdepth_dict_object:
        snowdepth_dict = snowdepth_dict_object.read()
        snowdepth_dict_object.close()
        snowdepth_dict = json.loads(snowdepth_dict)
        
    for value in temp_max_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_max += value
            cum_max_rec_days += 1
        else:
            cum_max_miss_days += 1
    
    daily_high_average = round((cum_max/cum_max_rec_days))
            
    print("The average daily high during ski season for the 1970s was {} degrees Fahrenheit.".format(daily_high_average))
    print('Data was missing for', cum_max_miss_days, 'out of', cum_max_rec_days+cum_max_miss_days, 'days.')

    for value in temp_min_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_min += value
            cum_min_rec_days += 1
        else:
            cum_min_miss_days += 1
            
    daily_low_average = round((cum_min/cum_min_rec_days))

    print("The average daily low during ski season for the 1970s was {} degrees Fahrenheit.".format(daily_low_average))
    print('Data was missing for', cum_min_miss_days, 'out of', cum_min_rec_days+cum_min_miss_days, 'days.')
    print('The average daily temperature spread was {} degrees Fahrenheit.'.format(daily_high_average - daily_low_average))
    
    for value in snowdepth_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_snowdepth += value
            cum_snow_rec_days += 1
        else:
            cum_snow_miss_days += 1
            
    snowdepth_average = round((cum_snowdepth/cum_snow_rec_days))
    
    print('The average daily snowdepth was {} inches.'.format(snowdepth_average))
    
    from collections import defaultdict
    merged_dict = defaultdict(list)
    dict_list = [temp_max_dict, temp_min_dict, snowdepth_dict]
    
    for dict in dict_list:
        for k, v in dict.items():
            merged_dict[k].append(v)
            
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s_data.json', 'w') as jsonfile:
            json.dump(merged_dict, jsonfile)
            

    with open('flarbin.csv', 'w') as flarbin:
        for key in merged_dict.keys():
            flarbin.write("%s,%s\n"%(key,merged_dict[key]))

monthly_temp_max_reader()
monthly_temp_min_reader()
monthly_snowdepth_reader()
search_function(query_results)

