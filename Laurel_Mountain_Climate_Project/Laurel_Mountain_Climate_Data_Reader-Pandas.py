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
from datetime import datetime

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
    
    df_1970s.to_csv('fa21python2_adam\\LM_Trivalues\\1970s_trivalue.csv')
    df_2000s.to_csv('fa21python2_adam\\LM_Trivalues\\2000s_trivalue.csv')
    df_all.to_csv('fa21python2_adam\\LM_Trivalues\\All_trivalue.csv')

    
    return df_1970s, df_2000s, df_all, min_temp_1970s_series

def user_interface():
    
    df_1970s, df_2000s, df_all, min_temp_1970s_series = dataframe_builder()
    pd.set_option('precision', 1)
    
    print('\n1. View 1970s summary data.\n2. View 2000s summary data.\n3. View combined summary data.\n4. Call up data for a single date.\n5. Call up data for a range of dates.\n6. Plot data from specified date range.')
    user_choice = input('What would you like to do (#, 1-5 or Q/q): ')

    acceptable_choices = ['1', '2', '3', '4', '5', '6']
    quits = ['Q', 'q']
    affirms = ['Y', 'y']
    denies = ['N', 'n']
    
    if user_choice in acceptable_choices:
        
        if user_choice == '1':
            print(df_1970s.describe())
            print('\nThis data set is saved in the directory LM_Trivalues as 1970s_trivalue.csv')
            user_interface()

        if user_choice == '2':
            print(df_2000s.describe())
            print('\nThis data set is saved in the directory LM_Trivalues as 2000s_trivalue.csv')
            user_interface()
            
        if user_choice == '3':
            print(df_all.describe())
            print('\nThis data set is saved in the directory LM_Trivalues as All_trivalue.csv')
            user_interface()
        
        if user_choice == '4':
            
            counter = 1
            while counter > 0:
                
                date_year = input('Enter a year (####): ')
                date_month = input('Enter a month (##): ')
                date_day = input('Enter a day (##): ')

                user_date = str(date_year+'-'+date_month+'-'+date_day)
                
                if user_date in df_all.index:
                    single_row = df_all.loc[user_date]
                    counter += -1
                    print(single_row)
                    write_option = input('Do you wish to write this data to a csv file?  Y/N: ')
                    if write_option in affirms:
                        print('\nFile saved as date.csv')
                        single_row.to_csv('fa21python2_adam\\'+user_date+'.csv', sep = ',', index=True, header=True)
                        
                    if write_option in denies:
                        print()
                        
                    if write_option in quits:
                        user_interface()
                else:
                    print('\nDate not found. Try another.')

            user_interface()
            
        if user_choice == '5':
            
            start_counter = 1
            end_counter = 1
            
            while start_counter > 0:
                
                start_date_year = input('Enter a starting year (####): ')
                start_date_month = input('Enter a starting month (##): ')
                start_date_day = input('Enter a starting day (##): ')
                
                start_date = str(start_date_year+'-'+start_date_month+'-'+start_date_day)
                
                start_ob = open('fa21python2_adam\\start_date.txt', 'w')
                start_ob.write(start_date)
                start_ob.close()
                
                df_1970s, df_2000s, df_all, min_temp_1970s_series = dataframe_builder()
                
                if start_date in df_all.index:
                    print('\nStart date found.')
                    start_counter += -1
                else:
                    print('\nDate not found. Try another.')
                
            while end_counter > 0:
                
                end_date_year = input('Enter an ending year (####): ')
                end_date_month = input('Enter an ending month (##): ')
                end_date_day = input('Enter an ending day (##): ')
                
                end_date = str(end_date_year+'-'+end_date_month+'-'+end_date_day)
                end_ob = open('fa21python2_adam\\end_date.txt', 'w')
                end_ob.write(end_date)
                end_ob.close()
                
                if end_date in df_all.index:
                    print('\nEnd date found.')
                    end_counter += -1
                else:
                    print('\nDate not found. Try another.')     
        
            sliced_df = df_all.loc[start_date:end_date]
            sliced_df.to_csv('fa21python2_adam\\workingdataset.csv', sep = ',', index=True, header=True)
            
            write_option = input('Do you wish to write this data set to a csv file?  Y/N: ')
            if write_option in affirms:
                print('\nFile saved as starting date-ending date.csv')
                sliced_df.to_csv('fa21python2_adam\\'+start_date+'-'+end_date+'.csv', sep = ',', index=True, header=True)
                
            if write_option in denies:
                pass
                
            if write_option in quits:
                user_interface()
            
            describe = input('Do you wish to view summary statistics for the specified date range?  Y/N: ')
            
            if describe in affirms:
                print()
                print(sliced_df.describe())
                
            write_me = input('Write summary statistics to file?  Y/N: ')
            if write_me in affirms:
                print('\nFile will be saved as starting date-ending date_summary_statistics.csv')
                sliced_df.describe().to_csv('fa21python2_adam\\'+start_date+'-'+end_date+'_summary_statistics.csv', sep=',', index=True, header=True, float_format='%.2f')
            
            if describe in denies:
                pass
                
            if describe in quits:
                func_quit()
                

                
        if user_choice == '6':
            plotter()
        
    if user_choice in quits:
        func_quit()
    
    else:
        user_interface()
        

def plotter():
    
    var_choices = ['1', '2', '3', '4', '5', '6', '7']
    quits = ['Q', 'q']
    
    start_ob = open('fa21python2_adam\\start_date.txt', 'r')
    start_date = start_ob.readline()
    start_date = datetime.fromisoformat(start_date)
    
    end_ob = open('fa21python2_adam\\end_date.txt', 'r')
    end_date = end_ob.readline()
    end_date = datetime.fromisoformat(end_date)
    
    df_1970s, df_2000s, df_all, min_temp_1970s_series = dataframe_builder()

    sliced_df = df_all.loc[start_date:end_date]
    
    var_count = input('\nIf you have not yet specified a date range during this session, the last date range used during the previous session will be plotted. Select variable(s): \n\n 1. Snow Depth\n 2. Minimum Temperature\n 3. Maximum Temperature\n 4. Snow Depth and Minimum Temperature\n 5. Snow Depth and Maximum Temperature\n 6. Minimum and Maximum Temperature\n 7. All\n\n Input (# or Q/q to return to main menu): ')
        
    if var_count in var_choices:
        
        if var_count == '1':
            plt.plot(sliced_df.iloc[:, 0], 'o')
            plt.show()
            
        if var_count == '2':
            plt.plot(sliced_df.iloc[:, 1])
            plt.show()
        
        if var_count == '3':
            plt.plot(sliced_df.iloc[:, 2])
            plt.show()
            
        if var_count == '4':
            plt.plot(sliced_df.iloc[:, 0:2])
            plt.show()

        if var_count == '5':
            plt.plot(sliced_df[['snow depth', 'max temp']])
            plt.show()
        
        if var_count == '6':
            plt.plot(sliced_df[['max temp', 'min temp']])
            plt.show()
            
        if var_count == '7':
            plt.plot(sliced_df)
            plt.show()
            
    if var_count in quits:
        user_interface()

    
def intro():
    
    quit_commands = ['Q', 'q']
    
    print('Welcome to the Laurel Mountain Climate Reader. This program provides statistical data on the maximum temperature, minimum temperature, and snowfall depth recorded at the weather station at Laurel Mountain, Pennsylvania (elevation 2,800\') from 12/1/1970 through 2/28/2013.  It can display these data for a given date, for the entire range of dates available, or for a user-specified range of dates; it can also provide summary data for user-specified date ranges. ')
    
    user_command = input('Press any key to proceed, or type Q or q to exit: ')
    
    if user_command not in quit_commands:
        print()
    
    if user_command in quit_commands: 
        func_quit()

def func_quit():
    sys.exit()
        
def main():

    #intro()
    temp_max_reader()
    temp_min_reader()
    snowdepth_reader()
    user_interface()


if __name__ == "__main__":
    main()


