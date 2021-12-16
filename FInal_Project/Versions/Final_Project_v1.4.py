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
    print(range_count)
    
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
    df_values = df_dict.values()
    
    for key in df_keys:
        df_dict[key] = df_dict[key].describe()

    for key in df_keys:
        df_dict[key] = pd.Series(df_dict[key].loc['mean'])
        
    snowfall_dict = {}
    
    for key in df_keys:
        snowfall_dict[key] = df_dict[key].loc['Snowfall']
    
    
    plt.plot(snowfall_dict.values())
    plt.show()
        



def main():

    #intro()
    #single_df_plotter()
    get_df_descriptions()


if __name__ == "__main__":
    main()