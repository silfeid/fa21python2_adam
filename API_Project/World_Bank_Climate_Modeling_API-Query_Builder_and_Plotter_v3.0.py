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
from matplotlib.pyplot import figure

figure(figsize=(12, 12), dpi=120)

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

def clear_startup_list():
    country_selection = open('fa21python2_adam/API_Project/country_set_selection.txt', 'w')
    country_selection.close()

def pick_countries():
    
    country_codes_df = load_country_codes()
    country_names = country_codes_df.index.tolist()
    country_choice_list = []
    
    quit_choices = ['Q', 'q', 'default']
    default = 'default'
    
    country_selection = open('fa21python2_adam/API_Project/country_set_selection.txt', 'a')
    
    country_choice = input('Type the name of a country to add it to the list. If you wish to use the default set of countries, type "default"; if you wish to view a list of the names of all countries available for analysis, type "show list".  Type Q/q to end list-making.\n\nCountry: ')
        
    while country_choice in country_names:
        country_choice_list.append(country_choice)
        country_choice = input('Pick a country, any country: ')
        
    for country in country_choice_list:
        country_selection.write(country+'\n')

    if country_choice not in country_names and country_choice not in quit_choices:
        print('\nNo such country, bub')
        country_selection.close()
        pick_countries()
        
    if country_choice in quit_choices:
        pass
    
    if country_choice == default:
        country_selection = open('fa21python2_adam/API_Project/country_set_selection.txt', 'w')
        country_selection.close()
        

def read_picked_countries():
    country_selection = open('fa21python2_adam/API_Project/country_set_selection.txt', 'r')    
    country_choice_list = country_selection.readlines()
    if not country_choice_list:
        country_choice_list = []
    new_country_choice_list = []

    for country in country_choice_list:
        country = country.strip('\n')
        new_country_choice_list.append(country)

    return new_country_choice_list

def get_year_and_country_lists():
    
    country_choice_list = read_picked_countries()
    country_codes_df = load_country_codes()
    country_codes_df['Country Name'] = country_codes_df.index
    country_codes_df = country_codes_df.set_index('Alpha-3 code')
    
    valid_choices = ['1', '2', '3']
    data_choice = input('Pick your data set: 1.a2 (worse case) 2. b1 (somewhat less bad) 3. Past (data 1900-2009)\n\nChoice: ')
        
    if data_choice in valid_choices:
        
        if data_choice == '1':
            filepath = 'fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_a2.csv'
            
        if data_choice == '2':
            filepath = 'fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_b1.csv'

        if data_choice == '3':
            filepath = 'fa21python2_adam/API_Project/Data_of_All_Nations/All_Past_Data.csv'

    country_data_df = pd.read_csv(filepath)
    
    country_data_df.columns = ['Country', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Year']
    
    rando = 0

    if not country_choice_list:
        
        rando = 1
        
    if country_choice_list:
        
        rando = 2
        
    if rando == 1:
        trunc_df = country_data_df.iloc[0:236:3]
        
    alpha3_choice_list = []
    country_data_df = country_data_df.set_index('Country')
    selected_year_list = []
        
    if rando == 2:
        
        for country in country_choice_list:
            alpha3_series = country_codes_df[country_codes_df['Country Name']==country]
            alpha3_code = alpha3_series[alpha3_series == country].index[0]
            alpha3_code = str(alpha3_code)

            alpha3_code = alpha3_code.replace('"', '')
            alpha3_code = alpha3_code.replace(' ', '')
            alpha3_choice_list.append(alpha3_code)
            
        for item in alpha3_choice_list:
            selected_year_list.append(country_data_df.loc[item, 'Year'])
            
        return country_choice_list, selected_year_list, data_choice
    
    if rando == 1:
        
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
        
        return wordy_country_list, year_list, data_choice
        
def difference_calculator():
    wordy_country_list_1, year_list_1, data_choice1 = get_year_and_country_lists()
    wordy_country_list_2, year_list_2, data_choice2 = get_year_and_country_lists()
    
    data_choices = 'Data Sets '+data_choice1+'-'+data_choice2
    
    unrounded_difference_list = [a - b for a, b in zip(year_list_1, year_list_2)]
    fahr_difference_list = []
    difference_list = []
    
    for temp in unrounded_difference_list:
        temp = float(temp)*(9/5)
        fahr_difference_list.append(temp)
    for temp in fahr_difference_list:
        temp = round(temp, 2)
        difference_list.append(temp)

    return difference_list, wordy_country_list_1, wordy_country_list_2, data_choices

def plotter():
    
    difference_list, wordy_country_list_1, wordy_country_list_2, data_choices = difference_calculator()


    plot_label_a = wordy_country_list_1[0]
    plot_label_b = wordy_country_list_1[-1]
    
    plot_label = plot_label_a+'-'+plot_label_b

    plt.bar(wordy_country_list_1, difference_list, color=['red'])
    plt.margins(0.01)
    plt.xticks(rotation =90)
    plt.xticks(fontsize = 10)
    for i in range(len(wordy_country_list_1)):
        plt.text(i,difference_list[i],difference_list[i], ha='center')
    plt.xlabel('Country', fontweight='bold', color = 'black', fontsize='12')
    plt.ylabel('Temperature Difference in Fahrenheit', fontweight='bold', color = 'black', fontsize='12')
    plt.tight_layout()
    plt.savefig('fa21python2_adam/API_Project/Plots/'+data_choices+'_('+plot_label+').jpg')
    plt.close()
    print('\nPlot successfully exported')
    
def func_quit():
    sys.exit()    

def what_next():
    whats_next = input('1. Do a different plot with the same set of countries.\n2. Add new countries.\n3. Clear countries list.\n\nChoice: ')
    valid_nexts = ['1', '2', '3']
    if whats_next in valid_nexts:
        if whats_next == '1':
            plotter()
            what_next()
        if whats_next == '2':
            pick_countries()
            plotter()
            what_next()
        if whats_next == '3':
            clear_startup_list()
            print('\nCountry List Cleared')
            what_next()
    
    
def main():
    clear_startup_list()
    print('Welcome to the climate reader.  I do things.')
    proceed = input('Type any key to proceed, or Q/q to quit.')
    quitters = ['Q', 'q']
    if proceed in quitters:
        print('\nBye then!')
        sys.exit()
    else:
        pick_countries()
        plotter()
        what_next()
    


if __name__ == "__main__":
    main()

