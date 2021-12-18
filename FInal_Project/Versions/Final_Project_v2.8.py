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
import matplotlib.dates as mdates
import sys
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import datetime

def build_dfs():
    
    directory = 'fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Snowdays_Only/'
    
    df_dict = {}
    
    for filename in os.listdir(directory):
    
        if filename.endswith('.csv'):
            filename = filename.replace('.csv', '')
            df_dict[filename] = pd.read_csv(directory+filename+'.csv')
            df_dict[filename] = df_dict[filename].set_index('ObDate')

    return df_dict

def integer_checker(slicer_datum):
  while True:
    try:
       user_input = int(input(slicer_datum))       
    except ValueError:
       print("Not a valid month/day/year! Try again.")
       continue
    else:
       return user_input 
       break 

def get_start_date():
    
    start_month = integer_checker('start month: ')
    if start_month > 0 and start_month < 13:
        pass
    else:
        print('Not a real month.  Try again.')
        start_month = integer_checker('start month: ')
    
    start_month = str(start_month)

    start_day = integer_checker('start day: ')

    thirtiers = ['9', '4', '6', '11']
    
    if start_month in thirtiers:
        while start_day > 30:
            start_day = integer_checker('start day: ')
            
    if start_month == 2:
        while start_day > 28:
            start_day = integer_checker('start day: ')
               
    else:
        while start_day > 31 or start_day < 0:
            start_day = integer_checker('start day: ')

    start_day = str(start_day)
            
    start_year = integer_checker('start year: ')
    
    if start_year < 1970 and start_year > 2013:
        print('Year must be between 1970 and 2013, inclusive. Try again.')
        start_year = integer_checker('start year: ')
    
    start_year = str(start_year)
    start_file = open('fa21python2_adam/Final_Project/Misc/starting_date.txt', 'w')
    start_file.write(start_month+'/'+start_day+'/'+start_year)
    start_file.close()
    
def get_end_date():
    
    end_month = integer_checker('end month: ')
    if end_month > 0 and end_month < 13:
        pass
    else:
        print('Not a real month.  Try again.')
        end_month = integer_checker('end month: ')
    
    end_month = str(end_month)

    end_day = integer_checker('end day: ')

    thirtiers = ['9', '4', '6', '11']
    
    if end_month in thirtiers:
        while end_day > 30:
            end_day = integer_checker('end day: ')
            
    if end_month == 2:
        while end_day > 28:
            end_day = integer_checker('end day: ')
               
    else:
        while end_day > 31 or end_day < 0:
            end_day = integer_checker('end day: ')

    end_day = str(end_day)
            
    end_year = integer_checker('end year: ')
    
    if end_year < 1970 and end_year > 2013:
        print('Year must be between 1970 and 2013, inclusive. Try again.')
        end_year = integer_checker('end year: ')
    
    end_year = str(end_year)
    end_file = open('fa21python2_adam/Final_Project/Misc/ending_date.txt', 'w')
    end_file.write(end_month+'/'+end_day+'/'+end_year)
    end_file.close()
    
def build_slicer_date():
    
   start_file = open('fa21python2_adam/Final_Project/Misc/starting_date.txt', 'r')
   start_date = start_file.read()
   
   end_file = open('fa21python2_adam/Final_Project/Misc/ending_date.txt', 'r')
   end_date = end_file.read()
   
   return start_date, end_date
   
def slice_dfs():
    
    df_dict = build_dfs()
    
    start, end = build_slicer_date()
    
    for df in df_dict.values():
        df.index = pd.to_datetime(df.index)
        
    for key in df_dict.keys():
        df_dict[key] = df_dict[key].loc[start:end]
    
    return df_dict, start, end

def single_df_plotter():
    
    df_dict, start, end = slice_dfs()
    station_choices = {1:'Dubois', 2:'Erie', 3:'Indiana', 4:'Laurel_Mountain', 5:'New_Castle', 6:'Pittsburgh', 7:'Uniontown', 8:'Warren'}
    df_name_choice = int(input('Pick a station for which to plot data:\n\n1.Dubois\n2.Erie\n3.Indiana\n4.Laurel Mountain\n5.New Castle\n6.Pittsburgh\n7.Uniontown\n8.Warren\n\nStation Choice: '))
    
    if df_name_choice in station_choices:
        df_name_chosen = station_choices[df_name_choice]
    
    df_choice = df_dict[df_name_chosen]
    df_fixed_name = df_name_chosen.replace('_', ' ')

    print()
    print('Station: '+df_name_chosen)

    plot_var_dict = {'1':'Snowfall', '2':'Snowdepth','3':'TempMin','4':'TempMax'} 
    print_var_dict = {'1':'Daily Snowfall', '2':'Daily Snow Depth','3':'Minimum Daily Temperature','4':'Maximum Daily Temperature'}
    
    plot_var_choice = input('Pick a variable for plotting: 1.Daily Snowfall 2. Daily Snow Depth 3. Minimum Daily Temperature 4. Maximum Daily Temperature Choice: ')
    print_var_choice = plot_var_choice
    print_variable = print_var_dict[print_var_choice]
    
    if int(plot_var_choice) < 3:
        print_unit = ' (in)'
    else:
        print_unit = ' (°F)'
    
    plot_variable = plot_var_dict[plot_var_choice]

    var_stat_plot = df_choice[plot_variable].plot(title=df_fixed_name+' '+print_variable+' '+start+'-'+end, xlabel='Year', ylabel=print_variable+print_unit, style='.', ms=3, figsize = (8, 4))
    
    start = start.replace('/', '.')
    end = end.replace('/', '.')

    fig = var_stat_plot.get_figure()
    fig.savefig('fa21python2_adam/Final_Project/Plots/Single_Stations/'+df_fixed_name+'_'+print_variable+'_'+start+'-'+end+'.jpg')
    plt.close(fig)
    print('\nPlot successfully exported to \'Plots/Single_Stations\'')   

def descriptive_stats_grapher():
    
    df_dict, start, end = slice_dfs()
    df_keys =list(df_dict.keys())
    
    for key in df_keys:
        df_dict[key] = df_dict[key].describe()

    for key in df_keys:
        df_dict[key] = pd.Series(df_dict[key].loc['mean'])
        
    for key in df_keys:
        df_dict[key] = df_dict[key].dropna()
        if df_dict[key].empty is True:
            del df_dict[key]
        
    df_keys = list(df_dict.keys())
        
    snowfall_dict = {}
    snowdepth_dict = {}
    tempmin_dict = {}
    tempmax_dict = {}
    
    for key in df_keys:
        if key in df_dict:
            snowfall_dict[key] = df_dict[key].loc['Snowfall']
        snowdepth_dict[key] = df_dict[key].loc['Snowdepth']
        tempmin_dict[key] = df_dict[key].loc['TempMin']      
        tempmax_dict[key] = df_dict[key].loc['TempMax']  
        
    for key in df_keys:
        snowfall_dict[key] = str(snowfall_dict[key])
        snowdepth_dict[key] = str(snowdepth_dict[key])
        tempmin_dict[key] = str(tempmin_dict[key])
        tempmax_dict[key] = str(tempmax_dict[key])

    for key in df_keys:
        if snowfall_dict[key] == 'nan':
            del snowfall_dict[key]
            if key in df_keys:
                df_keys.remove(key)
            else:
                pass
        if snowdepth_dict[key] == 'nan':
            del snowdepth_dict[key]
            if key in df_keys:
                df_keys.remove(key)
            else:
                pass
        if tempmin_dict[key] == 'nan':
            del tempmin_dict[key]
            if key in df_keys:
                df_keys.remove(key)
            else:
                pass            
        if tempmax_dict[key] == 'nan':
            del tempmax_dict[key]
            if key in df_keys:
                df_keys.remove(key)

            
    print(df_keys)
        
    for key in df_keys:
        snowfall_dict[key] = float(snowfall_dict[key])
        snowdepth_dict[key] = float(snowdepth_dict[key])
        tempmin_dict[key] = float(tempmin_dict[key])
        tempmax_dict[key] = float(tempmax_dict[key])    
    
    av_var_choice = input('Pick a variable and to see the graph of its average for each station.  Note that some stations reporting period is longer or shorter than others, so this comparison may be unequal.\n\n1. Average Daily Snowfall\n2. Average Daily Snow Depth\n3. Average Daily Minimum Temperature\n4. Average Daily Maximum Temperature\n\nChoice: ')
    
    valid_av_var_choices = ['1', '2', '3', '4']
    
    if av_var_choice in valid_av_var_choices:
        
        if av_var_choice == '1':
          
            snowfall_values = []
            snowfall_keys = []
            for value in snowfall_dict.values():
                value = round(value, 1)
                snowfall_values.append(value)
                
            mean_snowfall = (sum(snowfall_values))/(len(snowfall_values))
            mean_snowfall = round(mean_snowfall, 1)
            snowfall_values.append(mean_snowfall)
                               
            for key in snowfall_dict.keys():
                key = key.replace('_', ' ')
                snowfall_keys.append(key)                 
                
            snowfall_keys.append('All Stations Average')   
                             
            plt.bar(snowfall_keys, snowfall_values, color = 'skyblue')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Snowfall, All Stations '+start+'-'+end)
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(snowfall_values)):
                plt.text(item, snowfall_values[item], snowfall_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Snowfall (inches)', fontweight='bold', color = 'black', fontsize='12')            
            
            start = start.replace('/', '.')
            end = end.replace('/', '.')            
            
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/Means_Comparisons/Snowfall_All_Stations-'+start+'-'+end+'.jpg')
            print('\nFigure saved to directory \'Plots/All_Stations/Means_Comparisons\'')
            plt.close()
        
        if av_var_choice == '2':
          
            snowdepth_values = []
            snowdepth_keys = []
            for value in snowdepth_dict.values():
                value = round(value, 1)
                snowdepth_values.append(value)
                
            mean_snowdepth = (sum(snowdepth_values))/(len(snowdepth_values))
            mean_snowdepth = round(mean_snowdepth, 1)
            snowdepth_values.append(mean_snowdepth)    
                
            for key in snowdepth_dict.keys():
                key = key.replace('_', ' ')
                snowdepth_keys.append(key)       
                
            snowdepth_keys.append('All Stations Average')
        
            plt.bar(snowdepth_keys, snowdepth_values, color = 'thistle')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Snow Depth, All Stations '+start+'-'+end)
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(snowdepth_values)):
                plt.text(item, snowdepth_values[item], snowdepth_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Snow Depth (inches)', fontweight='bold', color = 'black', fontsize='12')        
            
            start = start.replace('/', '.')
            end = end.replace('/', '.')            
            
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/Means_Comparisons/Snow_Depth_All_Stations-'+start+'-'+end+'.jpg')
            print('\nFigure saved to directory \'Plots/All_Stations/Means_Comparisons\'')
            plt.close()
            
        if av_var_choice == '3':
          
            tempmin_values = []
            tempmin_keys = []
            
            for value in tempmin_dict.values():
                value = round(value, 1)
                tempmin_values.append(value)
                
            mean_tempmin = (sum(tempmin_values))/(len(tempmin_values))
            mean_tempmin = round(mean_tempmin, 1)
            tempmin_values.append(mean_tempmin)     
                
            for key in tempmin_dict.keys():
                key = key.replace('_', ' ')
                tempmin_keys.append(key)         
                
            tempmin_keys.append('All Stations Average')    
                
            plt.bar(tempmin_keys, tempmin_values, color = 'cadetblue')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Minimum Temperature, All Stations '+start+'-'+end)
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(tempmin_values)):
                plt.text(item, tempmin_values[item], tempmin_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Min Temp (°F)', fontweight='bold', color = 'black', fontsize='12')     
            
            start = start.replace('/', '.')
            end = end.replace('/', '.')            
            
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/Means_Comparisons/Temp_Min_All_Stations-'+start+'-'+end+'.jpg')
            print('\nFigure saved to directory \'Plots/All_Stations/Means_Comparisons\'')
            plt.close()

        if av_var_choice == '4':
          
            tempmax_values = []
            tempmax_keys = []
            
            for value in tempmax_dict.values():
                value = round(value, 1)
                tempmax_values.append(value)
                
            mean_tempmax = (sum(tempmax_values))/(len(tempmax_values))
            mean_tempmax = round(mean_tempmax, 1)
            tempmax_values.append(mean_tempmax)     
                
            for key in tempmax_dict.keys():
                key = key.replace('_', ' ')
                tempmax_keys.append(key)        
                
            tempmax_keys.append('All Stations Average')    
                
            plt.bar(tempmax_keys, tempmax_values, color = 'firebrick')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Maximum Temperature, All Stations '+start+'-'+end)
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(tempmax_values)):
                plt.text(item, tempmax_values[item], tempmax_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Max Temp (°F)', fontweight='bold', color = 'black', fontsize='12')         
            
            start = start.replace('/', '.')
            end = end.replace('/', '.')     
            
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/Means_Comparisons/Temp_Max_All_Stations-'+start+'-'+end+'.jpg')
            print('\nFigure saved to directory \'Plots/All_Stations/Means_Comparisons\'')
            plt.close()
   
                
def comparison_plotter():
#plots a single variable for all stations across the whole time period; so, 8 line plots, coded
#with different colors, on one graph...                
    df_dict, start, end = slice_dfs()
    df_keys = df_dict.keys()
    
    var_sel = input('Select a variable: \n1. Average Daily Snowfall\n2. Average Daily Snow Depth\n3. Average Daily Minimum Temperature\n4. Average Daily Maximum Temperature\n\nChoice: ')
    
    var_sel_choices = {'1':'Snowfall', '2':'Snowdepth', '3':'TempMin', '4':'TempMax'}
    var_sel_keys = var_sel_choices.keys()
                       
    if var_sel in var_sel_keys:
        var_sel = var_sel_choices[var_sel]
        
    for key in df_keys:
        df_dict[key] = df_dict[key][var_sel]

    for key in df_keys:
        df_dict[key] = pd.Series(df_dict[key], name = key)
        
    slice_keys = list(df_dict.keys())
    
    slicer = slice_keys[0]
        
    all_stations_df = pd.DataFrame(df_dict[slicer])
    
    for key in df_dict.keys():
        df_dict[key] = pd.Series(df_dict[key])
        
    for key, value in df_dict.items():
        value = pd.Series(value)
        all_stations_df = all_stations_df.merge(value, how='outer', left_index=True, right_index=True)
        
    fixed_var_sels = {'Snowdepth':'Daily Snow Depth', 'Snowfall':'Daily Snowfall', 'TempMin':'Daily Minimum Temperature', 'TempMax':'Daily Maximum Temperature'}
    
    if var_sel == 'TempMin' or var_sel == 'TempMax':
        unit = ' (Degrees Fahrenheit)'
    else:
        unit = ' (inches)'
                  
    all_stations_df.to_csv('fa21python2_adam/Final_Project/All_Stations.csv')        

    all_stations_df.drop('Dubois_x', axis=1, inplace=True)
    all_stations_df.rename(columns={'Dubois_y':'Dubois'}, inplace=True)
        
    all_stations_df = all_stations_df.reset_index()
    all_stations_df['ObDate'] = pd.to_datetime(all_stations_df['ObDate'])
    all_stations_df = all_stations_df.set_index('ObDate')
    all_stations_df = all_stations_df.sort_index()
    
    start = start.replace('/', '.')
    end = end.replace('/', '.')

    summary_stats = all_stations_df.describe()
    summary_stats.to_csv('fa21python2_adam/Final_Project/Summary_Stats_'+var_sel+'.csv')
    all_stations_plot = all_stations_df.plot(title='Historical '+fixed_var_sels[var_sel], xlabel='Year', ylabel=fixed_var_sels[var_sel]+unit, style='.', ms=4, figsize = (25, 10))
    
    fig = all_stations_plot.get_figure()
    fig.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/All_Stations_'+var_sel+'_'+start+'-'+end+'.png')
    plt.close()
    print('\nPlot saved in directory \'Plots/All_Stations\' with appropriate variable names.')

def correlation_plotter():

    df_dict, start, end = slice_dfs()
    df_keys = df_dict.keys()
    
    for key in df_keys:
        df_dict[key] = df_dict[key].describe()

    for key in df_keys:
        df_dict[key] = pd.Series(df_dict[key].loc['mean'])
        
    snowfall_dict = {}
    snowdepth_dict = {}
    tempmin_dict = {}
    tempmax_dict = {}
    
    for key in df_keys:
        snowfall_dict[key] = df_dict[key].loc['Snowfall']
        snowdepth_dict[key] = df_dict[key].loc['Snowdepth']
        tempmin_dict[key] = df_dict[key].loc['TempMin']      
        tempmax_dict[key] = df_dict[key].loc['TempMax']        
    
    stations_df = pd.read_csv('fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Stations/Stations.csv')
    
    snowfall_series = pd.Series(snowfall_dict)
    snowfall_series.name = 'Snowfall'

    stations_df['Snowfall'] = snowfall_dict.values()
    stations_df['Snowdepth'] = snowdepth_dict.values()    
    stations_df['TempMin'] = tempmin_dict.values()
    stations_df['TempMax'] = tempmax_dict.values()    

    means_series = stations_df.describe().loc['mean']
    
    lat_mean = means_series.loc['Latitude']
    elev_mean = means_series.loc['Elevation']
    
    lat_list = stations_df['Latitude'].to_list()
    elev_list = stations_df['Elevation'].to_list()
  
    lat_sd = stations_df.describe().at['std', 'Latitude']
    elev_sd = stations_df.describe().at['std', 'Elevation']
    
    lat_z_scores = []
    elev_z_scores = []
    
    for lat in lat_list:
        lat_z=(lat-lat_mean)/lat_sd
        lat_z_scores.append(lat_z)
        
    for elev in elev_list:
        elev_z=(elev-elev_mean)/elev_sd
        elev_z_scores.append(elev_z)    
    
    combined_z_scores = [(a + b)/2 for a, b in zip(lat_z_scores, elev_z_scores)]
        
    stations_df['Lat/El'] = combined_z_scores

    x_choices = {'1':'Latitude', '2':'Longitude', '3':'Elevation', '4':'Lat/El'}

    x_choice = input('Choose a variable to plot on the x axis: \n\n1.Latitude\n2.Longitude\n3.Elevation\n4.Weighted Average for Latitude and Elevation\n\nChoice: ')
    
    if x_choice in x_choices.keys():
        x_chosen = x_choices[x_choice]
    else:
        correlation_plotter()
        
    y_choices = {'1':'Snowfall', '2':'Snowdepth', '3':'TempMin', '4':'TempMax'}        
    y_choice = input('Choose a variable to plot on the y axis: \n\n1.Snowfall\n2.Snow Depth\n3.Minimum Temperature\n4.Maximum Temperature\n\nChoice: ')
    
    if y_choice in y_choices.keys():
        y_chosen = y_choices[y_choice]
    else:
        correlation_plotter()
        
    x = stations_df[x_chosen].to_list()
    y = stations_df[y_chosen].to_list()
    
    names = stations_df['StationName'].to_list()
    text = []
    
    if x_chosen == 'Latitude':
        x_units = ' (°N)'
    if x_chosen =='Longitude':
        x_units = ' (°W)'
    if x_chosen == 'Elevation':
        x_units = ' (feet above sea level)'    
    if x_chosen == 'Lat/El':
        x_units = ''
        x_chosen = 'Weighted Average for Latitude and Elevation'
    
    if y_chosen == 'Snowfall':
        y_units = ' (inches)'
    if y_chosen == 'Snowdepth':
        y_units = ' (inches)'
        y_chosen = 'Snow Depth'
    if y_chosen == 'TempMin' or y_chosen == 'TempMax':
        y_units = ' (degrees Fahrenheit)'
        
    for name in names:
        name = name.replace('_', ' ')
        text.append(name)

    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, s=10)
    
    title = x_chosen+' v. '+y_chosen+' Correlation Plot ('+start+'-'+end+')'
    
    plt.xlabel(x_chosen+x_units)
    plt.ylabel('Mean '+y_chosen+y_units)
    plt.title(title)
    
    start = start.replace('/', '.')
    end = end.replace('/', '.')
    
    title = x_chosen+' v. '+y_chosen+' Correlation Plot ('+start+'-'+end+')'
    
    for point in range(len(x)):
        plt.annotate(text[point], (x[point], y[point]))

    plt.tight_layout()
    plt.savefig('fa21python2_adam/Final_Project/Plots/Correlation_Plots/'+title+'.jpg')
    plt.show()

def menu():
    
    menu_choice = input('1.Pick date range (last used is default)\n2.Plot Precipitation and Snowfall Variables for a single station\n3.Compare averages across stations\n4.Compare a variable across all stations\n5.Plot correlations between station location and temperature and precipitation \n6.Quit\n\nChoice: ')
    
    menu_choices = ['0','1', '2', '3', '4', '5']
    
    if menu_choice in menu_choices:
        
        if menu_choice == '1':
            get_start_date()
            get_end_date()
            menu()
        
        if menu_choice == '2':
            single_df_plotter()
            menu()
        if menu_choice == '3':
            descriptive_stats_grapher()
            menu()
        if menu_choice == '4':
            comparison_plotter()
            menu()
        if menu_choice == '5':
            correlation_plotter()
            menu()
        if menu_choice == '6':
            func_quit()
            
    elif menu_choice == 'Q' or menu_choice == 'q':
        func_quit()
        
    else:
        print('\nInput not recognized.  Try again.')
        menu()

def func_quit():
    sys.exit()

def main():

    #intro()
    menu()
    #single_df_plotter()
    #descriptive_stats_grapher()
    #comparison_plotter()
    #correlation_plotter()
    #slice_dfs()


if __name__ == "__main__":
    main()