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

def temp_max_reader():
            
    directories = [r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\1970s', r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\2000s']
    
    save_count = 0
    
    for directory in directories:
        
        for filename in os.listdir(directory):
            if filename.endswith(".csv"):   
                with open(os.path.join(directory, filename), mode='r')\
                    as temp_file:
                    reader = csv.reader(temp_file)
                    temp_dict = {row[0]:row[1] for row in reader}
                    del temp_dict['Date']  
                    
                    if save_count == 0:
                        path = 'C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_max_data.json'
                    else:
                        path = 'C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_max_data.json'
                    
                    if os.path.exists(path) is True:
        
                        with open(path) as old_dict_object:
                            old_dict = old_dict_object.read()
                            old_dict_object.close()
                            old_dict = json.loads(old_dict)
                
                            old_dict.update(temp_dict)
                            updated_dict = old_dict
                
                    if os.path.exists(path) is False:
                        updated_dict = temp_dict
                    
                    with open(path, 'w') as jsonfile:
                            json.dump(updated_dict, jsonfile)
        save_count += 1
        
def temp_min_reader():
            
    directories = [r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\1970s', r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\2000s']
    
    save_count = 0
    
    for directory in directories:
        
        for filename in os.listdir(directory):
            if filename.endswith(".csv"):   
                with open(os.path.join(directory, filename), mode='r')\
                    as temp_file:
                    reader = csv.reader(temp_file)
                    temp_dict = {row[0]:row[2] for row in reader}
                    del temp_dict['Date']  
                    
                    if save_count == 0:
                        path = 'C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_min_data.json'
                    else:
                        path = 'C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_min_data.json'
                    
                    if os.path.exists(path) is True:
        
                        with open(path) as old_dict_object:
                            old_dict = old_dict_object.read()
                            old_dict_object.close()
                            old_dict = json.loads(old_dict)
                
                            old_dict.update(temp_dict)
                            updated_dict = old_dict
                
                    if os.path.exists(path) is False:
                        updated_dict = temp_dict
                    
                    with open(path, 'w') as jsonfile:
                            json.dump(updated_dict, jsonfile)
        save_count += 1
                               
def snowdepth_reader():
            
    directories = [r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\1970s', r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\2000s']
    
    save_count = 0
    
    for directory in directories:
        
        for filename in os.listdir(directory):
            if filename.endswith(".csv"):   
                with open(os.path.join(directory, filename), mode='r')\
                    as temp_file:
                    reader = csv.reader(temp_file)
                    temp_dict = {row[0]:row[-1] for row in reader}
                    del temp_dict['Date']  
                    
                    if save_count == 0:
                        path = 'C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\snowdepth_data.json'
                    else:
                        path = 'C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\snowdepth_data.json'
                    
                    if os.path.exists(path) is True:
        
                        with open(path) as old_dict_object:
                            old_dict = old_dict_object.read()
                            old_dict_object.close()
                            old_dict = json.loads(old_dict)
                
                            old_dict.update(temp_dict)
                            updated_dict = old_dict
                
                    if os.path.exists(path) is False:
                        updated_dict = temp_dict
                    
                    with open(path, 'w') as jsonfile:
                            json.dump(updated_dict, jsonfile)
        save_count += 1       
        
def dataframe_builder():
    
    snowdepth_1970s = pd.read_json('fa21python2_adam\\1970s\\snowdepth_data.json', typ='series')
    snowdepth_1970s_series = pd.Series(snowdepth_1970s, name='snow depth')
    
    snowdepth_1970s_series = pd.to_numeric(snowdepth_1970s_series, errors='coerce').dropna()
    
    max_temp_1970s = pd.read_json('fa21python2_adam\\1970s\\temperature_max_data.json', typ='series')
    max_temp_1970s_series = pd.Series(max_temp_1970s, name='max temp')
    
    max_temp_1970s_series = pd.to_numeric(max_temp_1970s_series, errors='coerce').dropna()
    
    min_temp_1970s = pd.read_json('fa21python2_adam\\1970s\\temperature_min_data.json', typ='series')
    min_temp_1970s_series = pd.Series(min_temp_1970s, name='min temp')
    
    min_temp_1970s_series = pd.to_numeric(min_temp_1970s_series, errors='coerce').dropna()
    
    snowdepth_2000s = pd.read_json('fa21python2_adam\\2000s\\snowdepth_data.json', typ='series')
    snowdepth_2000s_series = pd.Series(snowdepth_2000s, name='snow depth')
    
    snowdepth_2000s_series = pd.to_numeric(snowdepth_2000s_series, errors='coerce').dropna()
    
    max_temp_2000s = pd.read_json('fa21python2_adam\\2000s\\temperature_max_data.json', typ='series')
    max_temp_2000s_series = pd.Series(max_temp_2000s, name='max temp')
    
    max_temp_2000s_series = pd.to_numeric(max_temp_2000s_series, errors='coerce').dropna()
    
    min_temp_2000s = pd.read_json('fa21python2_adam\\2000s\\temperature_min_data.json', typ='series')
    min_temp_2000s_series = pd.Series(min_temp_2000s, name='min temp')
    
    min_temp_2000s_series = pd.to_numeric(min_temp_2000s_series, errors='coerce').dropna()
    
    df_1970s = pd.concat([snowdepth_1970s_series, min_temp_1970s_series, max_temp_1970s_series], axis=1)
    
    df_2000s = pd.concat([snowdepth_2000s_series, min_temp_2000s_series, max_temp_2000s_series], axis=1)
    
    all_snow = snowdepth_1970s_series.append(snowdepth_2000s_series)
    
    all_min = min_temp_1970s_series.append(min_temp_2000s_series)
    
    all_max = max_temp_1970s_series.append(max_temp_2000s_series)
    
    df_all = pd.concat([all_snow, all_min, all_max], axis=1)
    
    df_1970s.to_csv('fa21python2_adam\\1970s_trivalue.csv')
    df_2000s.to_csv('fa21python2_adam\\2000s_trivalue.csv')
    df_all.to_csv('fa21python2_adam\\all_trivalue.csv')
    
    return df_1970s, df_2000s, df_all

def user_interface():
    
    df_1970s, df_2000s, df_all = dataframe_builder()
    pd.set_option('precision', 1)
    
    print('\n1. View 1970s summary data.\n2. View 2000s summary data.\n3. View combined summary data.\n4. Call up data for a single date.\n5. Call up data for a range of dates.')
    user_choice = input('Well, pick, sonny: ')
    print()
    
    acceptable_choices = ['1', '2', '3', '4', '5', '6']
    quits = ['Q', 'q']
    
    if user_choice in acceptable_choices:
        
        if user_choice == '1':
            print(df_1970s.describe())
            user_interface()

        if user_choice == '2':
            print(df_2000s.describe())
            user_interface()
            
        if user_choice == '3':
            print(df_all.describe())
            user_interface()
        if user_choice == '4':
            
            counter = 1
            while counter > 0:
                
                date_year = input('Enter a year: ')
                date_month = input('Enter a month: ')
                date_day = input('Enter a day: ')
                
                
                user_date = str(date_year+'-'+date_month+'-'+date_day)
                
                if user_date in df_all.index:
                    print()
                    print(df_all.loc[user_date])
                    counter += -1
                else:
                    print('Ain\'t no such date in this here daytah-base, pard.  Try another.')
            print()
            user_interface()
    
    if user_choice in quits:
        func_quit()
    
    else:
        user_interface()
            
    
def intro():
    
    quit_commands = ['Q', 'q']
    
    print('Welcome to the Laurel Mountain Climate Reader. I do stuff.')
    
    user_command = input('Press any key to proceed, or type Q or q to exit: ')
    
    if user_command not in quit_commands:
        print()
    
    if user_command in quit_commands: 
        func_quit()

def func_quit():
    sys.exit()
        
def main():

    temp_max_reader()
    temp_min_reader()
    snowdepth_reader()
    print('Hey there pard.  Whatcha wanna do?\n')
    user_interface()


if __name__ == "__main__":
    main()


