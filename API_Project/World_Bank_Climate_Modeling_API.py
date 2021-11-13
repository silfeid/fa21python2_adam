# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:14:14 2021

@author: brode
"""

import requests
import json
import pandas as pd
import sys

def load_country_codes():
    #I downloaded a csv file listing all the UN-recognized countries and their respective ISO-Alpha-3 codes (some other data included too).  This came from GitHub, incidentally.  The function reads the csv into Python via Pandas as a DataFrame, which later on allows the program to "find" the country code associated with the country name that is solicited from the user in the pick_country() function below.  
    
    country_codes_df = pd.read_csv('fa21python2_adam/API_Project/countries_codes_and_coordinates.csv')
    
    country_codes_df = country_codes_df.set_index('Country')
    #Set the index to country names (i.e., the column labeled 'Country' in the header) so that we can retrieve the needed cell from the data frame using just the country name, rather than the integer indices, which no one is going to know without opening the .csv file on their own.
    return country_codes_df

def pick_country():
    #Solicits input from the user, asking them to type in the name of the country for which they wish to view data.  No input validation implemented yet - names must be typed exactly correctly, etc.  
    
    country = input('Type the name of the country for which you wish to view projected climate data: ')

    with open('fa21python2_adam/API_Project/country_choice.txt', 'w') as country_choice:
              country_choice.write(country)
              country_choice.close()
    #We write the name to file so that we can retrieve it conveniently later, to use in some set phrases given when the data is returned.
    
    return country

def read_country_name():
    #The function to retrieve the country name that we saved to a .txt file in the pick_country() function above.  Returns country_name as a variable (string) for use within other functions.
    
    country_choice = open('fa21python2_adam/API_Project/country_choice.txt', 'r')
    country_name = country_choice.read()
    country_choice.close()
    
    return country_name

def get_country_code():
    
#For some reason, I keep getting an error when I try to run the read_country_name() function within this function, the purpose of which should be self-evident.  So as a temporary fix I've stuck the code from the read_country_name() function here.  
    country_choice = open('fa21python2_adam/API_Project/country_choice.txt', 'r')
    country_name = country_choice.read()
    country_choice.close()
#After executing that, this function runs the load_country_codes() function to bring up the DataFrame containing those codes; it uses the "country_name" variable that we read from file as the index (row name) and the set column name 'Alpha-3 code' to retrieve the relevant country code (labeled as such).  
    country_codes_df = load_country_codes()
    
    country_code = country_codes_df.at[country_name, 'Alpha-3 code']
    
    country_code = country_code.replace('"', '')
    country_code = country_code.replace(' ', '')
#Then we strip out extraneous punctuation so as to be left with a pure string of three capital letters and return that variable (country_code) for use in main() below.
    
    return country_code

def main():
    
    pick_country()
    #User picks their country
    country_code = get_country_code()
    #We run get_country_code() to obtain the relevant code for the user's choice
    
    country_choice = open('fa21python2_adam/API_Project/country_choice.txt', 'r')
    country_name = country_choice.read()
    country_choice.close()
    #We run this code, which ought really to just be the read_country_name() function, but that seems to be broken for reasons that are currently beyond me.  Anyway, this does the same thing.
    
    request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/gfdl_cm2_1/tas/2020/2039/'+country_code+'.json'
    #We can finally use the country code variable to shape our request.  Only the text in the hyperlink following "v1" ever changes for request to this API.  "Country" means that we want data at the country level, rather than at the river-basin level.  "Mavg" means monthly average; "bccr_bcm2_0" indicates a particular model/methodology for climate prediction; this one has been created by  

    world_bank_API = requests.get(request)
    
    data = world_bank_API.text
    
    parsable_world_bank = json.loads(data)
    
    parsable_world_bank = pd.DataFrame(parsable_world_bank)
    
    parsable_world_bank.to_csv('fa21python2_adam/API_Project/'+country_code+'.csv')
    
    a2_monthly_values = parsable_world_bank.at[0, 'monthVals']
    
    b1_monthly_values = parsable_world_bank.at[1, 'monthVals']
    
    valid_choices = ['1', '2', '3', '4', '5']
    
    menu_choice = input('What would you like to do?\n\n1. Look at the predicted average monthly temperature for '+country_name+' for a given month in the bad scenario.\n2. Look at the predicted average monthly temperature for '+country_name+' for a given month in the less bad scenario.\n3. Look at the predicted average yearly temperature for '+country_name+' for a year in the selected range in the bad scenario.\n4. Look at the predicted average yearly temperature for '+country_name+' for a year in the selected range in the less bad scenario.\n5. Exit the program.\n\nSelection: ')
    
    if menu_choice in valid_choices:
        
        if menu_choice == '1':
            
            month = input('Enter the number of the month you want data for: ')
            month = int(month)
            month = month-1
            monthly_average = Fahrenheit_Converter(a2_monthly_values[month])
            monthly_average = str(monthly_average)
            
            if month == 0:
                month_name = 'January'
            if month == 1:
                month_name = 'February'
            if month == 2:
                month_name = 'March'
            if month == 3:
                month_name = 'April'
            if month == 4:
                month_name = 'May'
            if month == 5:
                month_name = 'June'
            if month == 6:
                month_name = 'July'
            if month == 7:
                month_name = 'August'
            if month == 8:
                month_name = 'September'
            if month == 9:
                month_name = 'October'
            if month == 10:
                month_name = 'November'
            if month == 11:
                month_name = 'December'
                
            past_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/month/'+country_code+'.json'
            
            past_data_API = requests.get(past_request)
    
            past_data = past_data_API.text
            
            parsable_past_data = json.loads(past_data)
            
            parsable_past_data = pd.DataFrame(parsable_past_data)
            
            past_average_celsius = parsable_past_data.at[month, 'data']
            
            past_average_fahrenheit = round((past_average_celsius*(9/5)+32), 2)
            
            print_past_average = str(past_average_fahrenheit)
            
            print('\nThe old average temperature for '+month_name+' (1901-2009) was '+print_past_average+' degrees Fahrenheit.')
                
            print('\nThe average temperature for '+month_name+' (2020-2039) will be: '+monthly_average+' degrees Fahrenheit.')
    
    else:
        pass
    
    if menu_choice == '2':
            
            month = input('Enter the number of the month you want data for: ')
            month = int(month)
            month = month-1
            monthly_average = str(Fahrenheit_Converter(b1_monthly_values[month]))

            if month == 0:
                month_name = 'January'
            if month == 1:
                month_name = 'February'
            if month == 2:
                month_name = 'March'
            if month == 3:
                month_name = 'April'
            if month == 4:
                month_name = 'May'
            if month == 5:
                month_name =  'June'
            if month == 6:
                month_name = 'July'
            if month == 7:
                month_name = 'August'
            if month == 8:
                month_name = 'September'
            if month == 9:
                month_name = 'October'
            if month == 10:
                month_name = 'November'
            if month == 11:
                month_name = 'December'
                
            past_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/month/'+country_code+'.json'
            
            past_data_API = requests.get(past_request)
    
            past_data = past_data_API.text
            
            parsable_past_data = json.loads(past_data)
            
            parsable_past_data = pd.DataFrame(parsable_past_data)
            
            past_average_celsius = parsable_past_data.at[month, 'data']
            
            past_average_fahrenheit = Fahrenheit_Converter(past_average_celsius)
            
            print_past_average = str(past_average_fahrenheit)
            
            print('\nThe old average temperature for '+month_name+' (1901-2009) was '+print_past_average+' degrees Fahrenheit.')
                
            print('\nThe average temperature for '+month_name+' (2020-2039) will be: '+monthly_average+' degrees Fahrenheit.')
    
    else:
        pass
    
    if menu_choice == '3':
        
        parsable_past_data = get_past_year_data()
        
        past_temp_series = pd.Series(parsable_past_data['data'])
        
        past_year_average = past_temp_series.mean()
        
        past_year_average = Fahrenheit_Converter(past_year_average)
        
        past_year_average = str(past_year_average)
        
        print('\nThe average temperature in '+country_name+' 1901-2009 was '+past_year_average+' degrees Fahrenheit.')
        
        future_temp_series = pd.Series(a2_monthly_values)
        
        future_year_average = future_temp_series.mean()
        
        future_year_average = Fahrenheit_Converter(future_year_average)
        
        future_year_average = str(future_year_average)
        
        print('\nThe average temperature in '+country_name+' 2020-2039 will be '+future_year_average+' degrees Fahrenheit, in the bad scenario.')
        
    if menu_choice == '4':
        
        parsable_past_data = get_past_year_data()
        
        past_temp_series = pd.Series(parsable_past_data['data'])
        
        past_year_average = past_temp_series.mean()
        
        past_year_average = Fahrenheit_Converter(past_year_average)
        
        past_year_average = str(past_year_average)
        
        print('\nThe average temperature in '+country_name+' 1901-2009 was '+past_year_average+' degrees Fahrenheit.')
        
        future_temp_series = pd.Series(b1_monthly_values)
        
        future_year_average = future_temp_series.mean()
        
        future_year_average = Fahrenheit_Converter(future_year_average)
        
        future_year_average = str(future_year_average)
        
        print('\nThe average temp5erature in '+country_name+' 2020-2039 will be '+future_year_average+' degrees Fahrenheit, in the less bad scenario.')
        
    if menu_choice == '5':
        func_quit()
        
def func_quit():
    sys.exit()

def Fahrenheit_Converter(temp):
    
    corrected_temp = round((temp*(9/5)+32), 2)
    
    return corrected_temp
 
def get_past_year_data():
    
        country_code = get_country_code()
    
        past_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/month/'+country_code+'.json'
            
        past_data_API = requests.get(past_request)

        past_data = past_data_API.text
        
        parsable_past_data = json.loads(past_data)
        
        parsable_past_data = pd.DataFrame(parsable_past_data)
        
        return parsable_past_data
        
if __name__ == "__main__":
    main()
