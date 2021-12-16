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

def build_dfs():
    
    directory = 'fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Snowdays_Only/'
    
    df_dict = {}
    
    for filename in os.listdir(directory):
    
        if filename.endswith('.csv'):
            filename = filename.replace('.csv', '')
            df_dict[filename] = pd.read_csv(directory+filename+'.csv')
            df_dict[filename] = df_dict[filename].set_index('ObDate')
    
    '''for dataframe_name in df_dict:
        print(dataframe_name)
        print(df_dict[dataframe_name])'''
        
    return df_dict

def single_df_plotter():
    
    df_dict = build_dfs()
    station_choices = {1:'Dubois', 2:'Erie', 3:'Indiana', 4:'Laurel_Mountain', 5:'New_Castle', 6:'Pittsburgh', 7:'Uniontown', 8:'Warren'}
    df_name_choice = int(input('Pick a station for which to plot data:\n\n1.Dubois\n2.Erie\n3.Indiana\n4.Laurel Mountain\n5.New Castle\n6.Pittsburgh\n7.Uniontown\n8.Warren\n\nStation Choice: '))
    
    if df_name_choice in station_choices:
        df_name_chosen = station_choices[df_name_choice]
    
    df_choice = df_dict[df_name_chosen]
    df_fixed_name = df_name_chosen.replace('_', ' ')

    print()
    print('Station: '+df_name_chosen)
    print()

    in_tag = ' in '  
    at_tag = ' at '
    
    plot_var_dict = {'1':'Snowfall', '2':'Snowdepth','3':'TempMin','4':'TempMax'} 
    print_var_dict = {'1':'Daily Snowfall', '2':'Daily Snow Depth','3':'Minimum Daily Temperature','4':'Maximum Daily Temperature'}
    
    plot_var_choice = input('Pick a variable for plotting: 1.Daily Snowfall 2. Daily Snow Depth 3. Minimum Daily Temperature 4. Maximum Daily Temperature Choice: ')
    print_var_choice = plot_var_choice
    print_variable = print_var_dict[print_var_choice]
    
    
    plot_variable = plot_var_dict[plot_var_choice]
       
    plt.plot(df_choice[plot_variable])
    
    at_stations = ['Laurel_Mountain']
    
    range_count = int(len(df_choice[plot_variable]))
    
    if df_name_chosen in at_stations:
        preposition = at_tag
    else:
        preposition = in_tag
        
    plot_title = 'Historical '+print_variable+preposition+df_fixed_name
    
    plt.title(plot_title, fontweight = 'bold', color = 'black', fontsize = '12')
    plt.xticks(np.arange(min(df_choice['Snowdepth']), max(df_choice['Snowdepth'])+range_count, 80.0)) #last number is the size of the step between ticks
    plt.xticks(rotation=70)
    plt.xticks(fontsize = 7)
    plt.yticks(fontsize = 7)
    plt.xlabel('\nDate', fontweight='bold', color = 'black', fontsize='8')
    plt.ylabel('Snow Depth in Inches\n', fontweight='bold', color = 'black', fontsize='8')
    plt.margins(0.01)
    plt.tight_layout()
    plt.savefig('fa21python2_adam/Final_Project/Plots/'+plot_title+'.jpg')
    plt.show()
    #Saved plot is totally blank - need to fix...
    plt.close()
    print('\nPlot successfully exported.')
    
#Make it so you can plot any one variable for all eight stations; but also
#generate wee df's from the describe func for each and then do a bar graph of 
#the mean of each datum.        
   
def get_df_descriptions():
    
    df_dict = build_dfs()
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
    
    av_var_choice = input('Pick a variable and to see the graph of its average for each station.  Note that some stations reporting period is longer or shorter than others, so this comparison may be unequal.\n\n1. Average Daily Snowfall\n2. Average Daily Snow Depth\n3. Average Daily Minimum Temperature\n4. Average Daily Maximum Temperature\n\nChoice: ')
    
    valid_av_var_choices = ['1', '2', '3', '4']
    
    if av_var_choice in valid_av_var_choices:
        
        if av_var_choice == '1':
          
            snowfall_values = []
            snowfall_keys = []
            for value in snowfall_dict.values():
                value = round(value, 1)
                snowfall_values.append(value)
            for key in snowfall_dict.keys():
                key = key.replace('_', ' ')
                snowfall_keys.append(key)                 
            plt.bar(snowfall_keys, snowfall_dict.values(), color = 'skyblue')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Snowfall, All Stations')
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(snowfall_values)):
                plt.text(item, snowfall_values[item], snowfall_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Snowfall (inches)', fontweight='bold', color = 'black', fontsize='12')              
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations_Comparison/Snowfall_All_Stations.jpg')
            print('Figure saved to \'Plots\' folder')            
            plt.show()
        
        if av_var_choice == '2':
          
            snowdepth_values = []
            snowdepth_keys = []
            for value in snowdepth_dict.values():
                value = round(value, 1)
                snowdepth_values.append(value)
            for key in snowdepth_dict.keys():
                key = key.replace('_', ' ')
                snowdepth_keys.append(key)                
            plt.bar(snowdepth_keys, snowdepth_dict.values(), color = 'thistle')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Snow Depth, All Stations')
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(snowdepth_values)):
                plt.text(item, snowdepth_values[item], snowdepth_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Snow Depth (inches)', fontweight='bold', color = 'black', fontsize='12')         
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations_Comparison/Snow_Depth_All_Stations.jpg')
            print('Figure saved to \'Plots\' folder')
            plt.show()
            
        if av_var_choice == '3':
          
            tempmin_values = []
            tempmin_keys = []
            for value in tempmin_dict.values():
                value = round(value, 1)
                tempmin_values.append(value)
            for key in tempmin_dict.keys():
                key = key.replace('_', ' ')
                tempmin_keys.append(key)                
            plt.bar(tempmin_keys, tempmin_dict.values(), color = 'cadetblue')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Minimum Temperature, All Stations')
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(tempmin_values)):
                plt.text(item, tempmin_values[item], tempmin_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Min Temp (Fahrenheit)', fontweight='bold', color = 'black', fontsize='12')         
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations_Comparison/Temp_Min_All_Stations.jpg')
            print('Figure saved to \'Plots\' folder')
            plt.show()

        if av_var_choice == '4':
          
            tempmax_values = []
            tempmax_keys = []
            for value in tempmax_dict.values():
                value = round(value, 1)
                tempmax_values.append(value)
            for key in tempmax_dict.keys():
                key = key.replace('_', ' ')
                tempmax_keys.append(key)                
            plt.bar(tempmax_keys, tempmax_values, color = 'firebrick')
            plt.xticks(rotation =60, fontsize = 10, ha = 'right')
            plt.title('Average Maximum Temperature, All Stations')
            plt.margins(0.1)
            plt.tight_layout()
            for item in range(len(tempmax_values)):
                plt.text(item, tempmax_values[item], tempmax_values[item], ha='center', rotation=0, verticalalignment='center_baseline')
            plt.xlabel('Station', fontweight='bold', color = 'black', fontsize='12')
            plt.ylabel('Max Temp (Fahrenheit)', fontweight='bold', color = 'black', fontsize='12')         
            plt.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/All_Stations_Means_Comparison/Temp_Max_All_Stations.jpg')
            print('Figure saved to \'Plots\' folder')
            plt.show()      
                
def comparison_plotter():
#plots a single variable for all stations across the whole time period; so, 8 line plots, coded
#with different colors, on one graph...                
    df_dict = build_dfs()
    df_keys = df_dict.keys()
    df_values = df_dict.values()
    
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
                   
#Really would be a lot better to turn this into a scatter plot...
    all_stations_df.to_csv('fa21python2_adam/Final_Project/All_Stations.csv')        

    all_stations_df.drop('Dubois_x', axis=1, inplace=True)
    all_stations_df.rename(columns={'Dubois_y':'Dubois'}, inplace=True)
        
    all_stations_df = all_stations_df.reset_index()
    all_stations_df['ObDate'] = pd.to_datetime(all_stations_df['ObDate'])
    all_stations_df = all_stations_df.set_index('ObDate')
    all_stations_df = all_stations_df.sort_index()

    summary_stats = all_stations_df.describe()
    summary_stats.to_csv('fa21python2_adam/Final_Project/Summary_Stats_'+var_sel+'.csv')
    all_stations_plot = all_stations_df.plot(title='Historical '+fixed_var_sels[var_sel], xlabel='Year', ylabel=fixed_var_sels[var_sel]+unit, style='.', ms=2, figsize = (25, 10))
    
    fig = all_stations_plot.get_figure()
    fig.savefig('fa21python2_adam/Final_Project/Plots/All_Stations/All_Stations_'+var_sel+'.png')
    

def correlation_plotter():
    
    df_dict = build_dfs()
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
    print(stations_df)    

    stations_df.plot.scatter(x='Latitude', y='Snowdepth', c='red')


#Next step is to allow slicing by date to compare one era/epoch/decade with another...




def main():

    #intro()
    #single_df_plotter()
    #get_df_descriptions()
    #comparison_plotter()
    correlation_plotter()
if __name__ == "__main__":
    main()