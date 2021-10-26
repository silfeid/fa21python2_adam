# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:57:50 2021

@author: brode
"""
import csv
import json
import os.path

directory = r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions'
    
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

    new_query_results = {}
    quit_commands = ['Q', 'q']

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
        
    query = input('Enter a date between 1/1/1970 and 2/28/2014 in order to view the maximum recorded temperature for that date (enter Q or q to exit): ')
    
    if query in temp_max_dict:
        
        daily_max_temp = temp_max_dict[query]
        if daily_max_temp.isnumeric():
            
            daily_max_temp = int(daily_max_temp)
            new_query_results[query] = daily_max_temp
            query_results.update(new_query_results)
     
        else:
            print('\nData is missing for that date, please try another.')
            
    if query in temp_min_dict:
        
        daily_min_temp = temp_min_dict[query]
        if daily_min_temp.isnumeric():
            
            daily_min_temp = int(daily_min_temp)
            new_query_results[query] = daily_min_temp
            query_results.update(new_query_results)
            
    if query in snowdepth_dict:
        
        snowdepth = snowdepth_dict[query]
        if snowdepth.isnumeric():
            
            snowdepth = int(snowdepth)
            new_query_results[query] = snowdepth
            query_results.update(new_query_results)
     
        else:
            print('\nData is missing for that date, please try another.')

    print('The maximum temperature that day was', daily_max_temp, 'degrees Fahrenheit.')
    print('The minimum temperature that day was', daily_min_temp, 'degrees Fahrenheit.')
    print('The average temperature that day was', (daily_min_temp + daily_max_temp)/2, 'degrees Fahrenheit.')   
    print('The temperature spread that day was', daily_max_temp - daily_min_temp, 'degrees Fahrenheit.')
    print('The snow depth was', snowdepth, 'inches.')
                   
    if query in quit_commands:
        print('\nThank you for using the Laurel Mountain Daily Temperature Database.')

    if query not in temp_max_dict or query not in temp_min_dict or query not in snowdepth_dict and query not in quit_commands:

        print('\nThat date is invalid or data for that month is missing from the database, try entering another.')

        search_function(query_results)         

    
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json', 'w') as jsonfile:
                json.dump(query_results, jsonfile)
    
    return query_results
            

monthly_temp_max_reader()
monthly_temp_min_reader()
monthly_snowdepth_reader()
search_function(query_results)

