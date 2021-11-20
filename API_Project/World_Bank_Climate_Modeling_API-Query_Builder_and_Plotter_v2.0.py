# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:14:49 2021

@author: brode
"""
import requests
import json
import pandas as pd
import sys
import os.path
import matplotlib.pyplot as plt
import seaborn as sns
import random

def load_country_codes():
    
    country_codes_df = pd.read_csv('fa21python2_adam/API_Project/countries_codes_and_coordinates.csv')
    
    country_codes_df = country_codes_df.set_index('Country')

    return country_codes_df

def get_country_codes():

    country_codes_df = load_country_codes()
    
    country_codes = country_codes_df['Alpha-3 code'].tolist()
    
    country_codes = [code.replace('"','') for code in country_codes]
    country_codes = [code.replace(' ','') for code in country_codes]

    return country_codes

def get_year_and_country_lists():
    
    country_codes_df = load_country_codes()
    country_codes_df['Country Name'] = country_codes_df.index
    country_codes_df = country_codes_df.set_index('Alpha-3 code')
    
    valid_choices = ['1', '2', '3']
    data_choice_one = input('Pick your data set: 1.a2 2. b1 3. Past\n\nChoice: ')
        
    if data_choice_one in valid_choices:
        
        if data_choice_one == '1':
            filepath = 'fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_a2.csv'
            
        if data_choice_one == '2':
            filepath = 'fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_b1.csv'

        if data_choice_one == '3':
            filepath = 'fa21python2_adam/API_Project/Data_of_All_Nations/All_Past_Data.csv'

    country_data_df = pd.read_csv(filepath)
    
    country_data_df.columns = ['Country', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Year']

    rando = random.randint(1,3)

    if rando == 1:
        trunc_df = country_data_df.iloc[0:78]
    if rando == 2:
        trunc_df = country_data_df.iloc[79:157]
    if rando == 3:
        trunc_df = country_data_df.iloc[158:236]
        
    year_df = trunc_df['Year']
    
    year_list = list(year_df)
    
    country_list = trunc_df['Country']
    country_list =list(country_list)

    wordy_country_list = []
    new_country_list = []
    
    for country in country_list:
        new_country = ' "'+country+'"'
        new_country_list.append(new_country)
    
    for new_country in new_country_list:
        wordy_country = country_codes_df.at[new_country, 'Country Name']
        wordy_country_list.append(wordy_country)
        
    return wordy_country_list, year_list
        
def difference_calculator():
    wordy_country_list_1, year_list_1 = get_year_and_country_lists()
    wordy_country_list_2, year_list_2 = get_year_and_country_lists()
    
    difference_list = [a - b for a, b in zip(year_list_1, year_list_2)]

    return difference_list, wordy_country_list_1, wordy_country_list_2


        
def plotter():
    
    difference_list, wordy_country_list_1, wordy_country_list_2 = difference_calculator()
    plt.bar(wordy_country_list_1, difference_list, color=['red'])
    plt.xticks(rotation =90)
    plt.xticks(fontsize = 4)
    
    plt.show()

plotter()


