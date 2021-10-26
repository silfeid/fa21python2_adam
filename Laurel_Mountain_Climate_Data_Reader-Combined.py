# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:57:50 2021

@author: brode
"""
import csv
import json
import os.path
import pandas
import matplotlib.pylab as plt

directory_A = r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\1970s'
directory_B = r'C:\Users\brode\Python\Laurel Mountain Historical Climate Data\CSV Versions\2000s'
    
query_results = {}

def monthly_temp_max_reader_2000s():
    
    for filename in os.listdir(directory_B):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory_B, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_max_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_max_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_max_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_max_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)
                        
def monthly_temp_max_reader_1970s():
    
    for filename in os.listdir(directory_A):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory_A, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_max_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_max_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_max_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_max_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)
                        
def monthly_temp_min_reader_2000s():
    
    for filename in os.listdir(directory_B):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory_B, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[2] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_min_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_min_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_min_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_min_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)

def monthly_temp_min_reader_1970s():
    
    for filename in os.listdir(directory_A):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory_A, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[2] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_min_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_min_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_min_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_min_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)
                        
def monthly_snowdepth_reader_2000s():
    
    for filename in os.listdir(directory_B):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory_B, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[-1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\snowdepth_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\snowdepth_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\snowdepth_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\snowdepth_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)
                        
def monthly_snowdepth_reader_1970s():
    
    for filename in os.listdir(directory_A):
        if filename.endswith(".csv"):   
            with open(os.path.join(directory_A, filename), mode='r')\
                as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[-1] for row in reader}
                del temp_dict['Date']  
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\snowdepth_data.json') is True:
    
                    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\snowdepth_data.json') as old_dict_object:
                        old_dict = old_dict_object.read()
                        old_dict_object.close()
                        old_dict = json.loads(old_dict)
            
                        old_dict.update(temp_dict)
                        updated_dict = old_dict
            
                if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\snowdepth_data.json') is False:
                    updated_dict = temp_dict
                
                with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\snowdepth_data.json', 'w') as jsonfile:
                        json.dump(updated_dict, jsonfile)

def snowdepth_plotter_1970s():
    with open('fa21python2_adam\\1970s\\1970s_data.csv', mode='r') as temp_file:
                reader = csv.reader(temp_file)
                temp_dict = {row[0]:row[-1] for row in reader}
                    
    
    myList = temp_dict.items()
    myList = sorted(myList) 
    x, y = zip(*myList) 
    
    plt.plot(x, y)
    plt.show()
    
    
    
    
def search_function_2000s(query_results):

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

    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_max_data.json') as temp_max_dict_object:
        temp_max_dict = temp_max_dict_object.read()
        temp_max_dict_object.close()
        temp_max_dict = json.loads(temp_max_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\temperature_min_data.json') as temp_min_dict_object:
        temp_min_dict = temp_min_dict_object.read()
        temp_min_dict_object.close()
        temp_min_dict = json.loads(temp_min_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\snowdepth_data.json') as snowdepth_dict_object:
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
    
    print('2000s SUMMARY')        
    print("\nThe average daily high during ski season for the 2000s was {} degrees Fahrenheit.".format(daily_high_average))
    print('Data was missing for', cum_max_miss_days, 'out of', cum_max_rec_days+cum_max_miss_days, 'days.\n')

    for value in temp_min_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_min += value
            cum_min_rec_days += 1
        else:
            cum_min_miss_days += 1
            
    daily_low_average = round((cum_min/cum_min_rec_days))

    print("The average daily low during ski season for the 2000s was {} degrees Fahrenheit.".format(daily_low_average))
    print('Data was missing for', cum_min_miss_days, 'out of', cum_min_rec_days+cum_min_miss_days, 'days.\n')
    print('The average daily temperature spread was {} degrees Fahrenheit.\n'.format(daily_high_average - daily_low_average))
    
    for value in snowdepth_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_snowdepth += value
            cum_snow_rec_days += 1
        else:
            cum_snow_miss_days += 1
            
    snowdepth_average = round((cum_snowdepth/cum_snow_rec_days))
    
    print('The average daily snowdepth was {} inches.'.format(snowdepth_average))
    print('Data was missing for', cum_snow_miss_days, 'out of', cum_snow_rec_days+cum_snow_miss_days, 'days.\n\n')
    
    corr_cum_min_miss_days = str(cum_min_miss_days)
    corr_cum_max_miss_days = str(cum_max_miss_days)
    corr_cum_min_days = str(cum_min_rec_days+cum_min_miss_days)
    corr_cum_max_days = str(cum_max_rec_days+cum_max_miss_days)
    corr_cum_snow_miss_days = str(cum_snow_miss_days)
    corr_cum_snow_days = str(cum_snow_rec_days+cum_snow_miss_days)
    
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\key_stats.txt', 'w') as key_stats_object:
        key_stats_object.write("The average daily high during ski season for the 2000s was {} degrees Fahrenheit.".format(daily_high_average))
        key_stats_object.write('\nData was missing for '+corr_cum_max_miss_days+' out of '+corr_cum_max_days+' days.')
        key_stats_object.write("\nThe average daily low during ski season for the 2000s was {} degrees Fahrenheit.".format(daily_low_average))
        key_stats_object.write('\nData was missing for '+corr_cum_min_miss_days+' out of '+corr_cum_min_days+' days.')
        key_stats_object.write('\nThe average daily temperature spread was {} degrees Fahrenheit.'.format(daily_high_average - daily_low_average))
        key_stats_object.write('\nThe average daily snowdepth was {} inches.'.format(snowdepth_average))
        key_stats_object.write('\nData was missing for '+corr_cum_snow_miss_days+' out of '+corr_cum_snow_days+' days.\n\n')
    
    from collections import defaultdict
    merged_dict = defaultdict(list)
    dict_list = [temp_max_dict, temp_min_dict, snowdepth_dict]
    
    for dict in dict_list:
        for k, v in dict.items():
            merged_dict[k].append(v)
            
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\2000s\\2000s_data.json', 'w') as jsonfile:
            json.dump(merged_dict, jsonfile)

    with open('fa21python2_adam\\2000s\\2000s_data.csv', 'w') as csv_2000s:
        
        for key in merged_dict.keys():
            csv_2000s.write("%s,%s\n"%(key,",".join(merged_dict[key])))
            
def search_function_1970s(query_results):

    cum_max = 0
    cum_max_rec_days = 0
    cum_max_miss_days = 0
    cum_min = 0
    cum_min_rec_days = 0
    cum_min_miss_days = 0
    cum_snowdepth = 0
    cum_snow_rec_days = 0
    cum_snow_miss_days = 0

    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_max_data.json') as temp_max_dict_object:
        temp_max_dict = temp_max_dict_object.read()
        temp_max_dict_object.close()
        temp_max_dict = json.loads(temp_max_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\temperature_min_data.json') as temp_min_dict_object:
        temp_min_dict = temp_min_dict_object.read()
        temp_min_dict_object.close()
        temp_min_dict = json.loads(temp_min_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\snowdepth_data.json') as snowdepth_dict_object:
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
    
    print('1970s SUMMARY')        
    print("\nThe average daily high during ski season for the 1970s was {} degrees Fahrenheit.".format(daily_high_average))
    print('Data was missing for', cum_max_miss_days, 'out of', cum_max_rec_days+cum_max_miss_days, 'days.')

    for value in temp_min_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_min += value
            cum_min_rec_days += 1
        else:
            cum_min_miss_days += 1
            
    daily_low_average = round((cum_min/cum_min_rec_days))

    print("\nThe average daily low during ski season for the 1970s was {} degrees Fahrenheit.".format(daily_low_average))
    print('Data was missing for', cum_min_miss_days, 'out of', cum_min_rec_days+cum_min_miss_days, 'days.')
    print('\nThe average daily temperature spread was {} degrees Fahrenheit.'.format(daily_high_average - daily_low_average))
    
    for value in snowdepth_dict.values():
        if value.isnumeric():
            value = int(value)
            cum_snowdepth += value
            cum_snow_rec_days += 1
        else:
            cum_snow_miss_days += 1
            
    snowdepth_average = round((cum_snowdepth/cum_snow_rec_days))
    
    print('\nThe average daily snowdepth was {} inches.'.format(snowdepth_average))
    print('Data was missing for', cum_snow_miss_days, 'out of', cum_snow_rec_days+cum_snow_miss_days, 'days.\n\n')
    
    corr_cum_min_miss_days = str(cum_min_miss_days)
    corr_cum_max_miss_days = str(cum_max_miss_days)
    corr_cum_min_days = str(cum_min_rec_days+cum_min_miss_days)
    corr_cum_max_days = str(cum_max_rec_days+cum_max_miss_days)
    corr_cum_snow_miss_days = str(cum_snow_miss_days)
    corr_cum_snow_days = str(cum_snow_rec_days+cum_snow_miss_days)

    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\key_stats.txt', 'w') as key_stats_object:
        key_stats_object.write("The average daily high during ski season for the 1970s was {} degrees Fahrenheit.".format(daily_high_average))
        key_stats_object.write('\nData was missing for '+corr_cum_max_miss_days+' out of '+corr_cum_max_days+' days.')
        key_stats_object.write("\nThe average daily low during ski season for the 1970s was {} degrees Fahrenheit.".format(daily_low_average))
        key_stats_object.write('\nData was missing for '+corr_cum_min_miss_days+' out of '+corr_cum_min_days+' days.')
        key_stats_object.write('\nThe average daily temperature spread was {} degrees Fahrenheit.'.format(daily_high_average - daily_low_average))
        key_stats_object.write('\nThe average daily snowdepth was {} inches.'.format(snowdepth_average))
        key_stats_object.write('\nData was missing for '+corr_cum_snow_miss_days+' out of '+corr_cum_snow_days+' days.\n\n')
    
    from collections import defaultdict
    merged_dict = defaultdict(list)
    dict_list = [temp_max_dict, temp_min_dict, snowdepth_dict]
    
    for dict in dict_list:
        for k, v in dict.items():
            merged_dict[k].append(v)
            
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\1970s\\1970s_data.json', 'w') as jsonfile:
            json.dump(merged_dict, jsonfile)
            
    with open('fa21python2_adam\\1970s\\1970s_data.csv', 'w') as csv_1970s:
        
        for key in merged_dict.keys():
            csv_1970s.write("%s,%s\n"%(key,",".join(merged_dict[key])))
            
def intro():
    
    quit_commands = ['Q', 'q']
    
    print('Welcome to the Laurel Mountain Climate Reader. I was created to resolve a trivial bet. I take National Weather Service data from the years 1970-1980 and 2003-2014 from the weather station at Laurel Mountain State Park in Western Pennsylvania and produce some statistics and records from it. My creator has gathered 72 csv files, 36 from each decade, with each file representing the climate data for one month of ski season during that decade (December-March inclusive). I read all those csv files and compile them, creating JSON files that link each individual datum that I\'m interested in (maximum temperature, minimum temperature, and snow depth) with a given date. Then I create one big dictionary that links each key (a date) to a value which is a list of the three data points listed above. I write that to JSON, then to CSV, and, after displaying some stats on the decade for my user (and writing these to a .txt file), I\'m done!')
    
    user_command = input('Press any key to proceed, or type Q or q to exit: ')
    
    if user_command not in quit_commands:
        print('\nHere we go!\n')
    
    if user_command in quit_commands: 
        func_quit()

def func_quit():
    sys.exit()
        
def main():
    
    intro()
    monthly_temp_max_reader_1970s()
    monthly_temp_min_reader_1970s()
    monthly_snowdepth_reader_1970s()
    search_function_1970s(query_results)
    monthly_temp_max_reader_2000s()
    monthly_temp_min_reader_2000s()
    monthly_snowdepth_reader_2000s()
    search_function_2000s(query_results)
    snowdepth_plotter_1970s()

if __name__ == "__main__":
    main()


