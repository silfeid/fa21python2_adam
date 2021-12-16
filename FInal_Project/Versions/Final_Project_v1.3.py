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
import sys
import numpy as np

def build_snow_dfs():
    
    directory = 'fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Snowdays_Only/'
    
    df_dict = {}
    
    for filename in os.listdir(directory):
    
        if filename.endswith('.csv'):
            filename = filename.replace('.csv', '')
            df_dict[filename] = pd.read_csv(directory+filename+'.csv')
            df_dict[filename] = df_dict[filename].set_index('ObDate')
    
    for dataframe_name in df_dict:
        print(dataframe_name)
        print(df_dict[dataframe_name])
        
    return df_dict
        
def single_df_plotter():
    
    df_dict = build_snow_dfs()
    station_choices = {1:'Dubois', 2:'Erie', 3:'Indiana', 4:'Laurel_Mountain', 5:'New_Castle', 6:'Pittsburgh', 7:'Uniontown', 8:'Warren'}
    df_name_choice = int(input('Pick a station for which to plot data:\n\n1.Dubois\n2.Erie\n3.Indiana\n4.Laurel Mountain\n5.New Castle\n6.Pittsburgh\n7.Uniontown\n8.Warren\n\nStation Choice: '))
    
    if df_name_choice in station_choices:
        df_name_chosen = station_choices[df_name_choice]
    
    df_choice = df_dict[df_name_chosen]
    df_fixed_name = df_name_chosen.replace('_', ' ')
    print()
    print('Station: '+df_name_chosen)
    print()
    print(df_choice.describe())
    
    in_tag = 'in '
    
    at_tag = 'at '
    
    plot_variable = input('Pick

    plt.plot(df_choice['Snowdepth'])
    
    at_stations = ['Laurel_Mountain']
    
    if df_name_chosen in at_stations:
        preposition = at_tag
    else:
        preposition = in_tag
        
    plot_title = 'Historical'+
    
    plt.title('Historical Snow Depth '+preposition+df_fixed_name, fontweight = 'bold', color = 'black', fontsize = '12')
    plt.xticks(np.arange(min(df_choice['Snowdepth']), max(df_choice['Snowdepth'])+2300, 100.0))
    plt.xticks(rotation=90)
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.xlabel('\nDate', fontweight='bold', color = 'black', fontsize='8')
    plt.ylabel('Snow Depth in Inches\n', fontweight='bold', color = 'black', fontsize='8')
    plt.margins(0.01)
    plt.tight_layout()
    plt.savefig('fa21python2_adam/Final_Project/Plots/'+Snowdepth.jpg')
    plt.show()
    #Saved plot is totally blank - need to fix...
    plt.close()
    print('\nPlot successfully exported.')
    
#Make it so you can plot any one variable for all eight stations; but also
#generate wee df's from the describe func for each and then do a bar graph of 
#the mean of each datum.        
    

def main():

    #intro()
    single_df_plotter()

if __name__ == "__main__":
    main()