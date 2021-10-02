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

def monthly_temp_data_reader():
    
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)

def results_dumper():
    if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json') is True:
        with open('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json') as old_query_object:
            old_query = old_query_object.read()
            old_query_object.close()
            old_query = json.loads(old_query)
    
            old_query.update(temp_query)
            updated_query = old_query
            
    if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\query_resultse_data.json') is False:
            updated_query = temp_query
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json', 'w') as jsonfile:
                json.dump(updated_query, jsonfile)
    

    
def search_function(query_results):

    new_query_results = {}

    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_data.json') as finished_dict_object:
        finished_dict = finished_dict_object.read()
        finished_dict_object.close()
        finished_dict = json.loads(finished_dict)
        
    query = input('Enter a date between 1/1/1970 and 2/28/2014 in order to view the maximum recorded temperature for that date (enter Q or q to exit): ')
    
    query == str(query)
    
    if query in finished_dict:
        
        daily_temp = finished_dict[query]
        if daily_temp.isnumeric():
            
            print(daily_temp, 'degrees Fahrenheit was the maximum temperature recorded on', query)
            new_query_results[query] = daily_temp
            query_results.update(new_query_results)
            print(query_results)
            search_function(query_results)
            
        else:
            print('\n')
            print('Data is missing for that date, please try another.')
            search_function(query_results)
                   
    if query != 'Q' or query != 'q' and query in finished_dict:
        
        print('\n')
        print('That date is invalid or data for that month is missing from the database, try entering another.')
        print(query_results)
        search_function(query_results)

    if query == 'Q' or query == 'q':
        print('\n')
        print('Thank you for using the Laurel Mountain Daily Temperature Database')                

    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json', 'w') as jsonfile:
                json.dump(query_results, jsonfile)
    
    return query_results
            

monthly_temp_data_reader()
search_function(query_results)

