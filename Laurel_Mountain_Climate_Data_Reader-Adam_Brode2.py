# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:57:50 2021

@author: brode
"""
import csv
import json
import os.path

def monthly_temp_data_reader():
    
    with open('C:\\Users\\brode\\Python\\Laurel Mountain Historical Climate Data\\LaurelMountainTempsDecember1972.csv', mode='r')\
        as temp_file:
        reader = csv.reader(temp_file)
        temp_dict = {row[0]:row[1] for row in reader}
        del temp_dict['Date']  
    
    return temp_dict

def json_dumper():
       
    temp_dict = monthly_temp_data_reader()
    
    if os.path.exists('C:\\Users\\brode\\Python\\temp_data.json') is True:
    
        with open('C:\\Users\\brode\\Python\\temp_data.json') as old_dict_object:
            old_dict = old_dict_object.read()
            old_dict_object.close()
            old_dict = json.loads(old_dict)

            old_dict.update(temp_dict)
            updated_dict = old_dict
    
    if os.path.exists('C:\\Users\\brode\\Python\\temp_data.json') is False:
        updated_dict = temp_dict
    
    print("The Master of Ballantrae")
    
    with open('temp_data.json', 'w') as jsonfile:
            json.dump(updated_dict, jsonfile)
            print("file written")
        


monthly_temp_data_reader()
json_dumper()

