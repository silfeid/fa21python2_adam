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

def get_past_year_data():
    #A little function to grab the historical climate data for a given country; there's only one scenario (past is solitary, future myriad) and only one range of dates 1901-2009, so all we need is the country code and we can assemble the DataFrame we'll need, which is what this function returns.  For more information on that, cf. the top of main().
    
    country_code = get_country_code()

    past_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/month/'+country_code+'.json'
        
    past_data_API = requests.get(past_request)

    past_data = past_data_API.text
    
    parsable_past_data = json.loads(past_data)
    
    parsable_past_data = pd.DataFrame(parsable_past_data)
    
    return parsable_past_data

def main():
    
    pick_country()
    #User picks their country
    country_code = get_country_code()
    #We run get_country_code() to obtain the relevant code for the user's choice
    
    country_choice = open('fa21python2_adam/API_Project/country_choice.txt', 'r')
    country_name = country_choice.read()
    country_choice.close()
    #We run this code, which ought really to just be the read_country_name() function, but that seems to be broken for reasons that are currently beyond me.  Anyway, this does the same thing.
    
    request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/bccr_bcm2_0/tas/2020/2039/'+country_code+'.json'
    #We can finally use the country code variable to shape our request.  Only the text in the hyperlink following "v1" ever changes for request to this API.  "Country" means that we want data at the country level, rather than at the river-basin level.  "Mavg" means monthly average; "bccr_bcm2_0" indicates a particular model/methodology for climate prediction; this one has been created bythe Bjerknes Centre for Climate Research (BCCR), Univ. of Bergen, Norway.  "Tas" indicates average temperature in celsisus;2020 is the start date, 2039 is the end date, country_code is self-obvious, and .json specifies the format in which to return the data.

    world_bank_API = requests.get(request)
    #Fetch the data from the API
    
    data = world_bank_API.text
    #Honestly not all that sure what this does, since I'd think the data already existed in text format, but apparently this is something that needs to happen.
    
    parsable_world_bank = json.loads(data)
    #load that data up into json so Python understands it
    
    parsable_world_bank = pd.DataFrame(parsable_world_bank)
    #And convert it from .json to a Pandas DataFrame, which *I* can understand.
    
    parsable_world_bank.to_csv('fa21python2_adam/API_Project/'+country_code+'.csv')
    #Writing the DataFrame to csv just in case we want to access it later - not strictly necessary, but I thought it couldn't hurt.  Could implement a feature where the program checks first to see whether the relevant csv data for that country is already present in the home directory before initiating a request for it through the API.
    
    a2_monthly_values = parsable_world_bank.at[0, 'monthVals']
    #The API returns data for two scenarios, a2 and b1.  You can read up on them here:  .  A2 is pretty bad, b1 somewhat less so.  I'm separating the data (12 monthly temperature values, the predicted average for each month in the selected country) into two , one for each scenario.  This is the a2 list...
    
    b1_monthly_values = parsable_world_bank.at[1, 'monthVals']
    #And here we have the b1 list.
    
    valid_choices = ['1', '2', '3', '4', '5']
    #For input validation, although this hasn't even really been implemented yet.  
    
    menu_choice = input('What would you like to do?\n\n1. Look at the predicted average monthly temperature for '+country_name+' for a given month in the bad scenario.\n2. Look at the predicted average monthly temperature for '+country_name+' for a given month in the less bad scenario.\n3. Look at the predicted average yearly temperature for '+country_name+' for a year in the selected range in the bad scenario.\n4. Look at the predicted average yearly temperature for '+country_name+' for a year in the selected range in the less bad scenario.\n5. Exit the program.\n\nSelection: ')#User menu, inserting the name of the selected country into formula text.
    if menu_choice in valid_choices:
        
        if menu_choice == '1':
            
            month = input('Enter the number of the month you want data for: ')
            #I could/should fix this so the user can type the number or name, but for now, just the number 1-12 seems adequate.  No input validation here yet either.
            month = int(month)
            #Turn that string into an int so that we can perform a very simply calculation on it.
            month = month-1
            #Subtract one from whatever the user entered so as to translate the int value to Pythonese; now we can use whatever month number they typed in as an index by which to slice our list of monthly temperature values.
            monthly_average = Fahrenheit_Converter(a2_monthly_values[month])
            #We retrieve the desired monthly value from our "a2_monthly_values" list using integer variable "month" as our index for slicing, then run it through the Fahrenheit_Converter() function (see below), because: 'Murika.
            monthly_average = str(monthly_average)
            #And now we'll convert that number to a string for printing.  This step maybe could just be bundled into the Fahrenheit Converter, but I wanted to preserve the ability to perform arithmetic operations on the Fahrenheit number as well.
            
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
                
            #Just a quick check to convert the numeric month to the actual English month name, since no one says "on the Fourth of Seven," etc.  We'll use "month_name" in some formulaic text printouts below.
                
            past_request = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/month/'+country_code+'.json'
            #Now we run a slightly different request to get historic data for the same country; this data is 1901-2009 and comes from the World Bank's Climate Research Unit (The CRU in the request).
            
            past_data_API = requests.get(past_request)
    
            past_data = past_data_API.text
            
            parsable_past_data = json.loads(past_data)
            
            parsable_past_data = pd.DataFrame(parsable_past_data)
            
            past_average_celsius = parsable_past_data.at[month, 'data']
            #So, all the same code as before, just formatted for past data.  For some reason the relevant column here is labeled "data" instead of "monthVals", but otherwise it's all the same.
            
            past_average_fahrenheit = Fahrenheit_Converter(past_average_celsius)
            
            print_past_average = str(past_average_fahrenheit)
            
            print('\nThe old average temperature for '+month_name+' (1901-2009) was '+print_past_average+' degrees Fahrenheit.')
            #So now we have what we need to print the old temperature average in that country for that month...
                
            print('\nThe average temperature for '+month_name+' (2020-2039) will be '+monthly_average+' degrees Fahrenheit.')
            #And the new one.
    
    else:
        pass
    
    if menu_choice == '2':
            #So, all of this code is exactly the same as for menu_choice 1, except that it runs its operations on the list we created for the b1 model, rather than for the a2 model as above.  So I'm not going to comment further; cf. the equivalent code above if needed.
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
                
            print('\nThe average temperature for '+month_name+' (2020-2039) will be '+monthly_average+' degrees Fahrenheit.')
    
    else:
        pass
    
    if menu_choice == '3':
        #So, this step is very similar to what we've been doing above, but slightly easier since we don't have to index by month.
        
        parsable_past_data = get_past_year_data()
        #Runs the get_past_year_data() function to retrieve a DataFrame with the relevant data.
        
        past_temp_series = pd.Series(parsable_past_data['data'])
        #Make a series out of the one column that we care about.
        
        past_year_average = past_temp_series.mean()
        #From our monthly data (12 data points) we just get the mean so we have the yearly average.
        
        past_year_average = Fahrenheit_Converter(past_year_average)
        #Make it Fahrenheit
        
        past_year_average = str(past_year_average)
        #String it up
        
        print('\nThe average temperature in '+country_name+' 1901-2009 was '+past_year_average+' degrees Fahrenheit.')
        
        future_temp_series = pd.Series(a2_monthly_values)
        #Now we do pretty much the same thing; we turn our a2_monthly_values list into a Series in Pandas, not because we truly have to (we could calculate the average for the list with a for loop, for example), but because the .mean() function in Pandas is handy and easy.
        
        future_year_average = future_temp_series.mean()
        #So we grab that average from the a2 data.
        
        future_year_average = Fahrenheit_Converter(future_year_average)
        #Make it so 'Murricans can unnerstan!
        
        future_year_average = str(future_year_average)
        #String it up
        
        print('\nThe average temperature in '+country_name+' 2020-2039 will be '+future_year_average+' degrees Fahrenheit, in the bad scenario.')
        
    if menu_choice == '4':
        #And this is all just the same as for menu_choice 3 above, with the b1 scenario data subbed in for the a2 scenario.  Otherwise identical.
        
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
    #Function to let the user easily quit.
    sys.exit()

def Fahrenheit_Converter(temp):
    #Pretty self-evident
    corrected_temp = round((temp*(9/5)+32), 2)   
    return corrected_temp

        
if __name__ == "__main__":
    main()
