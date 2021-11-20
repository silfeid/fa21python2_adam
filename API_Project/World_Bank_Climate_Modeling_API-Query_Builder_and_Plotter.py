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

def a2_plotter():
    
    country_codes_df = load_country_codes()
    country_codes_df['Country Name'] = country_codes_df.index
    country_codes_df = country_codes_df.set_index('Alpha-3 code')

    all_future_data_a2_df = pd.read_csv('fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_a2.csv')
    
    all_future_data_a2_df.columns = ['Country', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Year']
    
    trunc_df = all_future_data_a2_df.iloc[0:100]
    year_df = trunc_df['Year']
    year_list = list(year_df)
    cunt_list = trunc_df['Country']
    cunt_list =list(cunt_list)

    wordy_cunt_list = []
    new_cunt_list = []
    
    for cunt in cunt_list:
        new_cunt = ' "'+cunt+'"'
        new_cunt_list.append(new_cunt)
    
    for new_cunt in new_cunt_list:
        wordy_cunt = country_codes_df.at[new_cunt, 'Country Name']
        wordy_cunt_list.append(wordy_cunt)
        
    print(wordy_cunt_list)
    
    years = year_list
    cunts = wordy_cunt_list
    plt.bar(cunts, years, color=['red'])
    plt.xticks(rotation =90)
    plt.xticks(fontsize = 4)
    print('\n\nTemperatures in the a2 scenario')
    
    plt.show()

a2_plotter()


