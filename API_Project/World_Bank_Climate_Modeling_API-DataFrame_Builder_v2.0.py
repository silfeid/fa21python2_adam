# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:43:10 2021

@author: brode
"""

import requests
import json
import pandas as pd
import sys
import os.path

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

def get_past_year_data():

    country_codes = get_country_codes()

    directory = r'C:/Users/brode/Python/fa21python2_adam/API_Project/Data_of_All_Nations/Past_Data'
    
    for filename in os.listdir(directory):
        for country_code in country_codes:
            if filename.startswith(country_code):   
                country_codes.remove(country_code)
    
    if not country_codes:
        print('All done, bub!')
        
    else:
        
        for country_code in country_codes:
            
            past_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/month/'+country_code+'.json'
                
            past_data_API = requests.get(past_request)
            
            past_data = past_data_API.text
            
            if past_data == 'Invalid country code. Three letters are required':
                with open('fa21python2_adam/API_Project/Data_of_All_Nations/Missing_Nations.txt', 'a') as missing_nations:
                    missing_nations.write(country_code+'\n')
                    
            else:
            
                past_data_df = json.loads(past_data)
                
                past_data_df = pd.DataFrame(past_data_df)
                
                if past_data_df.empty:
                    pass
                else:
                    past_data_df.to_csv('fa21python2_adam/API_Project/Data_of_All_Nations/Past_Data/'+country_code+'.csv')
            
def get_future_year_data_a2():
    
    country_codes = get_country_codes()
    country_codes.sort()
    directory = r'C:\Users\brode\Python\fa21python2_adam\API_Project\Data_of_All_Nations\Future_Data\a2'
    
    for filename in os.listdir(directory):
        for country_code in country_codes:
            if filename.startswith(country_code):   
                country_codes.remove(country_code) 
    if not country_codes:
        print('All done, bub!')
    else:
        
        for country_code in country_codes:
            
            future_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/gfdl_cm2_1/tas/2020/2039/'+country_code+'.json'
                
            future_data_API = requests.get(future_request)
            
            future_data = future_data_API.text
            
            if future_data == 'Invalid country code. Three letters are required':
                with open('fa21python2_adam/API_Project/Data_of_All_Nations/Missing_Nations.txt', 'a') as missing_nations:
                    missing_nations.write(country_code+'\n')
            
            else:
                
                future_data_df = json.loads(future_data)            
                future_data_df = pd.DataFrame(future_data_df)                
                a2_monthly_values = future_data_df.at[0, 'monthVals']                
                a2_monthly_df = pd.DataFrame(a2_monthly_values)                

                a2_monthly_df.index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                a2_monthly_df.columns = ['temperature']

                a2_monthly_df.to_csv('fa21python2_adam/API_Project/Data_of_All_Nations/Future_Data/a2/'+country_code+'.csv')

def get_future_year_data_b1():

    country_codes = get_country_codes()
    country_codes.sort()
    directory = r'C:\Users\brode\Python\fa21python2_adam\API_Project\Data_of_All_Nations\Future_Data\b1'
    
    for filename in os.listdir(directory):
        for country_code in country_codes:
            if filename.startswith(country_code):   
                country_codes.remove(country_code) 
    if not country_codes:
        print('All done, bub!')
    else:
        
        for country_code in country_codes:
            
            future_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/gfdl_cm2_1/tas/2020/2039/'+country_code+'.json'
                
            future_data_API = requests.get(future_request)
            
            future_data = future_data_API.text
            
            if future_data == 'Invalid country code. Three letters are required':
                with open('fa21python2_adam/API_Project/Data_of_All_Nations/Missing_Nations.txt', 'a') as missing_nations:
                    missing_nations.write(country_code+'\n')
            
            else:
                
                future_data_df = json.loads(future_data)            
                future_data_df = pd.DataFrame(future_data_df)                
                a2_monthly_values = future_data_df.at[1, 'monthVals']                
                a2_monthly_df = pd.DataFrame(a2_monthly_values)                

                a2_monthly_df.index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                a2_monthly_df.columns = ['temperature']

                a2_monthly_df.to_csv('fa21python2_adam/API_Project/Data_of_All_Nations/Future_Data/b1/'+country_code+'.csv')
                        
def build_df_from_past_series():
    
    df_of_all_nations_past = pd.DataFrame()
    directory = r'C:/Users/brode/Python/fa21python2_adam/API_Project/Data_of_All_Nations/Past_Data'
    
    for item in os.listdir(directory):
        
        temp_series = pd.read_csv('fa21python2_adam/API_Project/Data_of_All_Nations/Past_Data/'+item)
        name = item.strip('.csv')
        temp_series = temp_series.T
        temp_series = temp_series.drop('month', axis=0)
        
        temp_series.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        temp_series = temp_series.drop(temp_series.index[0])                      
        temp_series.index = [name]
        temp_series['Year'] = ((temp_series['January']+temp_series['February']+temp_series['March']+temp_series['April']+temp_series['May']+temp_series['June']+temp_series['July']+temp_series['August']+temp_series['September']+temp_series['October']+temp_series['November']+temp_series['December'])/12)

        df_of_all_nations_past = df_of_all_nations_past.append(temp_series, ignore_index=False)
        
    df_of_all_nations_past.to_csv('fa21python2_adam/API_Project/Data_of_All_Nations/All_Past_Data.csv')
    
def build_df_from_future_series_a2():
    
    df_of_all_nations_a2 = pd.DataFrame()
    
    directory = r'C:\Users\brode\Python\fa21python2_adam\API_Project\Data_of_All_Nations/Future_Data/a2'
    
    for item in os.listdir(directory):
        
        temp_series = pd.read_csv('fa21python2_adam\API_Project\Data_of_All_Nations/Future_Data/a2/'+item)
        name = item.strip('.csv')
        temp_series = temp_series.drop(temp_series.columns[0], axis=1)
        temp_series = temp_series.T
        temp_series.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                               
        temp_series.index = [name]
        temp_series['Year'] = ((temp_series['January']+temp_series['February']+temp_series['March']+temp_series['April']+temp_series['May']+temp_series['June']+temp_series['July']+temp_series['August']+temp_series['September']+temp_series['October']+temp_series['November']+temp_series['December'])/12)

        df_of_all_nations_a2 = df_of_all_nations_a2.append(temp_series, ignore_index=False)
        
    df_of_all_nations_a2.to_csv('fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_a2.csv')
    
def build_df_from_future_series_b1():
    
    df_of_all_nations_b1 = pd.DataFrame()
    
    directory = r'C:\Users\brode\Python\fa21python2_adam\API_Project\Data_of_All_Nations/Future_Data/b1'
    
    for item in os.listdir(directory):
        
        temp_series = pd.read_csv('fa21python2_adam\API_Project\Data_of_All_Nations/Future_Data/b1/'+item)
        name = item.strip('.csv')
        temp_series = temp_series.drop(temp_series.columns[0], axis=1)
        temp_series = temp_series.T
        temp_series.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                               
        temp_series.index = [name]
        temp_series['Year'] = ((temp_series['January']+temp_series['February']+temp_series['March']+temp_series['April']+temp_series['May']+temp_series['June']+temp_series['July']+temp_series['August']+temp_series['September']+temp_series['October']+temp_series['November']+temp_series['December'])/12)

        df_of_all_nations_b1 = df_of_all_nations_b1.append(temp_series, ignore_index=False)
        
    df_of_all_nations_b1.to_csv('fa21python2_adam/API_Project/Data_of_All_Nations/All_Future_Data_b1.csv')
        
get_past_year_data()
build_df_from_past_series()   
get_future_year_data_a2()
build_df_from_future_series_a2()
get_future_year_data_b1()
build_df_from_future_series_b1()
