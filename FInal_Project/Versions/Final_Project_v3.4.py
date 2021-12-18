# -*- coding: utf-8 -*-
"""
Created on Fri December 10 20:55:41 2021

@author: Adam Brode (brodeam@gmail.com) 

Boilerplate explanation goes here.
"""
#os.path will be used to pull files from a specified directory according to certain criteria, and to create directories for storing saved plots based on the names of the dataframes plotted.
import os.path
#Pandas is used to create the dataframes from .csv files, to generally  manipulate the data, create new dataframes from the starting set, and to plot (via matplotlib)
import pandas as pd
#Matplotlib.pyplot is used for plotting, in some instances directly, in others Pandas 'piggybacks' on it in order to plot a dataframe.
import matplotlib.pyplot as plt
#Sys is used only for the func_quit() function, which does just what you'd think it does.  It quits.  Some say it's the best at quitting.
import sys
#This is just to allow me to adjust the plotting parameters to autolayout, below.
from matplotlib import rcParams
#datetime alows strings ina  given format to be interpreted as datetime (or here, just date) objects; although pandas has a similar function built-in, here I wanted to compare the starting and ending dates by which the user can slice the dataframes, in order to make sure that the specified end date does not precede the specified start date.  In hindsight, I could probably also have used it to control the input for those dates, instead of the exception handling function for integers that I built on, but oh well.  If it ain't broke...
from datetime import datetime as dt

#The auto-layout feature should prevent some text etc. from being cut-off; I figured better safe than sorry, and it seems to at least not have caused any problems.
rcParams.update({'figure.autolayout': True})

#This function does what you'd think:  it builds the dataframes that will be used to conduct most of the subsequent calculation and visualization.
def build_dfs():
    
    #The individual station .csv files, downloaded from https://www.ncdc.noaa.gov/, were manipulated in MS SQL Server, where they constitute a relational database, and then saved in their final form in the directory below.
    directory = 'fa21python2_adam/Final_Project/Climate_Data/Daily_Climate_Data/Snowdays_Only/'
    
    #An empty dictionary, to be populated with station names as keys and dataframes as values.
    df_dict = {}
    
    #this for loop iterates over all of the files in the directory, and if they end in .csv (they all should, but one never knows), then it uses the read_csv function built into Pandas to turn them into dataframes, using the filename as the name of the dataframe - the keys in the dictionary referenced above (df_dict).
    for filename in os.listdir(directory):
    
        if filename.endswith('.csv'):
            #Get rid of the .csv so we can have the station name alone as the key 
            filename = filename.replace('.csv', '')
            #Add .csv back to the path so that it'll read properly
            df_dict[filename] = pd.read_csv(directory+filename+'.csv')
            #Set the ObDate Column (Observation Date) as the index; these are also the primary keys for the tables in the SQL Database; StationCode is the foreign key that relates to the Stations table, containing geographic information on each station.
            df_dict[filename] = df_dict[filename].set_index('ObDate')
    
    #The next bit of code uses the os module to create new directories at a specified location (within parent_dir), one for each station location identified above.        
    parent_dir = "fa21python2_adam/Final_Project/Plots/Single_Stations/"
    
    #Each key represents a station, so we just iterate over the keys in this for loop.
    for key in list(df_dict.keys()):
        
        #the filepath for the new directory = the parentdir + the key name
        path = os.path.join(parent_dir, key)
        #Check to make sure that directory doesn't already exit; if it does, we simply "pass" ;this way new stations can be added to the database/program without creating a headache.
        if os.path.isdir(path) is False:
            #os.mkdir creates a directory at the specified filepath
            os.mkdir(path)
        else:
            pass
    #Return the df_dict, which we'll use throughout the rest of the program
    return df_dict

#The integer checker just checks input from the user and as you've already guessed, makes sure that it's an integer; if it's not, a message is displayed and the user is prompted once more. At this stage, any integer will do.
def integer_checker(slicer_datum):
  while True:
    try:
       user_input = int(input(slicer_datum))       
    except ValueError:
       print("\nInput must be an integer. Try again.")
       continue
    else:
       return user_input 
       break 
#Here, we'll use the integer checker to solicit a start date from the user.  Once we get an integer, we can perform the necessary checks to make sure that it's a valid month, valid day for that month, and valid year.
def get_start_date():
    
    print('Pick the date range for which you wish to plot data.  The first available date is January 1, 1970; the last available date is December 31, 2013.')
    #Run integer checker to get our user input.
    start_month = integer_checker('Select starting month: ')
    #Should be pretty clear; needs to be an integer that corresponds to a month.
    if start_month > 0 and start_month < 13:
        pass
    else:
        print('\nMust be integer 1-12. Try again.')
        start_month = integer_checker('Select starting month: ')
    
    #Now that the necessary operations have been performed, we onvert the start_month to a string so that it can be concatenated and written to a .txt file as needed.
    start_month = str(start_month)
    
    #Pretty similar operations are performed on the start_day variable, as below, mutatis mutandis etc. etc.
    start_day = integer_checker('Select starting day: ')

    thirtiers = ['9', '4', '6', '11']
    
    if start_month in thirtiers:
        while start_day > 30 and start_day <32:
            print('\nDay does not match to month')
            start_day = integer_checker('Select starting day: ')
            
    if start_month == '2':
        print(start_month)
        while start_day > 28:
            print('\nDay does not match to month; leap days are excluded from this program.')
            start_day = integer_checker('Select starting day: ')
               
    else:
        while start_day > 31 or start_day < 0:
            print('\nNo month has that number of days in it.')
            start_day = integer_checker('Select starting day: ')

    start_day = str(start_day)
    
    #And grab the start year; here, we just make sure it's not before 1970 or after 2013.        
    start_year = integer_checker('Select starting year: ')
    
    if start_year < 1970 or start_year > 2013:
        print('\nYear must be between 1970 and 2013, inclusive. Try again.')
        start_year = integer_checker('Select starting year: ')
    
    start_year = str(start_year)
    
    #We concatenate the start month, day, and year to get our start_date, adding the slashes as needed...
    start_date = start_month+'/'+start_day+'/'+start_year
    #And write that date to a .txt file, so that it can be summoned by the program even after restarting (the last used date, i.e. the date last written to the .txt file, is the default start date used by the program; same goes for the end date, below.)
    start_file = open('fa21python2_adam/Final_Project/Misc/starting_date.txt', 'w')
    start_file.write(start_date)
    start_file.close()
    
    print('\nStarting date successfully chosen.  Next, pick an ending date.')

#This function works almost identically to the get_start_date() function above, so only those aspects which differ between the two are commented on below.
def get_end_date():
    
    #Read the start_date in from the .txt file, since we need to compare it to the end date to make sure that the latter doesn't come before the former, chronologically
    start_file = open('fa21python2_adam/Final_Project/Misc/starting_date.txt', 'r')
    start_date = start_file.read()
    #And here we use the datetime module and its strptime function to parse a string as a datetime object (here, just a date, as specified by the .date() tag at the end the function).
    check_start_date = dt.strptime(start_date, '%m/%d/%Y').date()
    
    end_month = integer_checker('Select ending month: ')
    if end_month > 0 and end_month < 13:
        pass
    else:
        print('\nMust be integer 1-12. Try again.')
        end_month = integer_checker('Select ending month: ')
    
    end_month = str(end_month)

    end_day = integer_checker('Select ending day: ')

    thirtiers = ['9', '4', '6', '11']
    
    if end_month in thirtiers:
        while end_day > 30 and end_day <32:
            print('\nDay does not match to month')
            end_day = integer_checker('Select ending day: ')
            
    if end_month == '2':
        print(end_month)
        while end_day > 28:
            print('\nDay does not match to month; leap days are excluded from this program.')
            end_day = integer_checker('Select ending day: ')
               
    else:
        while end_day > 31 or end_day < 0:
            print('\nNo month has that number of days in it.')
            end_day = integer_checker('Select ending day: ')

    end_day = str(end_day)
            
    end_year = integer_checker('Select ending year: ')
    
    if end_year < 1970 or end_year > 2013:
        print('\nYear must be between 1970 and 2013, inclusive. Try again.')
        end_year = integer_checker('Select ending year: ')
        
    end_year = str(end_year)
    
    end_date = end_month+'/'+end_day+'/'+end_year
    #Here we turn the end_date into a datetime object as well...
    check_end_date = dt.strptime(end_date, '%m/%d/%Y').date()
    #...And use a simple comparison operator to determine that it does indeed come after the start date and not before.  If it didn't, we'd just start the get_end_date function over after displaying a message telling the user what they did wrong.
    if check_end_date < check_start_date:
        print('\nEnd date must come after start date!')
        get_end_date()
    
    else:
        
        end_file = open('fa21python2_adam/Final_Project/Misc/ending_date.txt', 'w')
        end_file.write(end_date)
        end_file.close()
        
        print('\nEnding date successfully chosen.')

#This function retrieves the starting and ending dates saved to .txt via their respective functions.  Using this method allows us to simply retrieve the last dates used if the user doesn't wish to enter new ones, giving a default set of dates.    The code here should be self-explanatory.
def build_slicer_date():
    
   start_file = open('fa21python2_adam/Final_Project/Misc/starting_date.txt', 'r')
   start_date = start_file.read()
   
   end_file = open('fa21python2_adam/Final_Project/Misc/ending_date.txt', 'r')
   end_date = end_file.read()
   
   return start_date, end_date
#This wee function simply prints the current start and end dates selected in case the user has forgotten them or is using the program for the first time (for them).
def show_slicer_dates():
    start_date, end_date = build_slicer_date()
    print('\nStart date: '+start_date)
    print('End date: '+end_date)

#Having built our dataframes, we now use the start and end dates arrived at above to slice each dataframe by index (which you'll remember we set to the 'ObDate' column earlier), so that each dataframe is truncated to include only those dates (ObDates) which fall in the range specified by the user.   
def slice_dfs():
    #Retrieve the dataframes
    df_dict = build_dfs()
    #Retrieve the start and end dates.
    start, end = build_slicer_date()
    #Up to this point, the ObDate column (our index for each dataframe) has been in the format of a string; this step converts it to datetime object, something that's thankfully built into Pandas and which Pandas can readily interpret.  Note that although it retains its former name when the dataframe is displayed, the ObDate column can only be summoned as df.index once it's been set as such, and can't be called using its former column name (ObDate).
    for df in df_dict.values():
        df.index = pd.to_datetime(df.index)
    #Thankfully Pandas is smart, and although 'start' and 'end' are just strings formatted in the same way as our datetime objects in ObDate/index, Pandas recognizes them as such when we use them to slice the index; the for loop below does this for each dataframe, summoning it from the dictionary using the name of its key and then slicing use the .loc function of Pandas.    
    for key in df_dict.keys():
        df_dict[key] = df_dict[key].loc[start:end]
    #We will want the start and end dates later, not to manipulate the df's (that step's done with), but to use as variables in displaying plots and in creating unique filenames for saving.  Since we're not working with any unsliced df's (the user simply picks the first and last available dates if they wish to view data for the entire date range), we'll just replace the old df_dict with this one.
    return df_dict, start, end

#This function plots one of the four variables charted in each dataframe, all of them daily: Snowfall, Snow Depth, Minimum Temperature and maximum Temperature, for a single station.  The user will first pick which station they want to view, then which variable.
def single_df_plotter():
    
    #Grab the df's and start, end dates from the slice_dfs() function
    df_dict, start, end = slice_dfs()
    
    #I used a dictionary of the station names to control user input; they'll just pick a number from the list printed below and the dictionary is then used to transform that into the actual station name/dictionary key needed.
    station_choices = {1:'Butler', 2:'Clarion', 3:'Confluence', 4:'Dubois', 5:'Erie', 6:'Franklin', 7:'Indiana', 8:'Laurel_Mountain', 9:'New_Castle', 10:'Pittsburgh', 11:'Tionesta', 12:'Uniontown', 13:'Warren', 14:'Waynesburg'}
    
    print('Pick a station for which to plot data:\n\n1.Butler\n2.Clarion\n3.Confluence\n4.Dubois\n5.Erie\n6.Franklin\n7.Indiana\n8.Laurel Mountain\n9.New Castle\n10.Pittsburgh\n11.Tionesta\n12.Uniontown\n13.Warren\n14.Waynesburg')
    #The integer checker from above is used to validate user input here as well.
    df_name_choice = integer_checker('\nStation Choice: ')
                                
    #If they picked an integer that corresponds to a station, we summon the value associated with that integer key here.
    if df_name_choice in station_choices:
        df_name_chosen = station_choices[df_name_choice]
    #If they entered an invalid integer, then we return them to the main menu after telling them what they did wrong.  Restarting the function will produce errors which I don't quite grok as yet.
    else:
        print('Not a valid station number. Try again.')
        menu()
    
    #Summon the dataframe we want from df_dict as "df_choice"
    df_choice = df_dict[df_name_chosen]
    #Here we create a 'fixed' name for the names that have an underscore in them where there would normally be a space (i.e., those station names which are two or more words).  In hindsight, I probably could have just left the spaces in from the beginning, but oh well.
    df_fixed_name = df_name_chosen.replace('_', ' ')

    #This probably can be deleted, but just a print statement to confirm to the user which station they've chosen.
    print('\nStation: '+df_name_chosen)

    #A dictionary of the variables for plotting, on the model of the one above for stations.
    plot_var_dict = {1:'Snowfall', 2:'Snowdepth',3:'TempMin', 4:'TempMax'} 
    
    #Versions of the same variables for 'pretty printing' (display on the plots, saving, etc.)
    print_var_dict = {'1':'Daily Snowfall', '2':'Daily Snow Depth','3':'Minimum Daily Temperature','4':'Maximum Daily Temperature'}
    
    plot_var_choice = integer_checker('Pick a variable for plotting: 1.Daily Snowfall 2. Daily Snow Depth 3. Minimum Daily Temperature 4. Maximum Daily Temperature Choice: ')
    
    #Same mechanism as above for input validation: boot 'em to the main menu if the integer isn't appropriate...I'm 100% sure there's a better way to do this, but as I mentioned above, restarting the function itself produces unexpected errors, and I'm pretty much out of time at this point...perfect enemy of good mumble mumble...
    
    
    if plot_var_choice in plot_var_dict:
        pass
        
    else:
        print('Choice not valid.  Returning to main menu.')
        menu()
    
    #We'll turn that int to a string and use it grab the correct print variable from the print variable dictionary we created a few lines above.  Just so it'll look all nice later on.
    plot_var_choice = str(plot_var_choice)
    print_variable = print_var_dict[print_var_choice]
    
    #Picking what units to display on the y axis of the plot (below); since choices one and two for plot_var are measured in inches, and 3 and 4 are measured in degrees Fahrenheit, the if clause here is pretty simple.
    if int(plot_var_choice) < 3:
        print_unit = ' (in)'
    else:
        print_unit = ' (°F)'
    
    #Use our plot variable choice to grab the right column name from the plot var dictionary we created at the start of the function code.
    plot_variable = plot_var_dict[plot_var_choice]

    #We use the plot variable uh...variable (a string) to select the appropriate column from our chosen dataframe and plot it using Pandas; if we ask Pandas to plot a single column, i.e., a Series, it will automatically use the index as the x-axis and the values in the series as the y-axis, handily setting the ticks and scale all by itself.  Below I've used the variables that I created above to assign the plot a title containing relevant information and labels for the x and y axes.  Ms stands for marker size, and figsize is x*y dimensions, I believe in inches.  Seems that way anyway.  Certainly isn't cm.  Maybe hundreds of pixels?  I dunno.
    var_stat_plot = df_choice[plot_variable].plot(title=df_fixed_name+' '+print_variable+' '+start+'-'+end, xlabel='Year', ylabel=print_variable+print_unit, style='.', ms=6, figsize = (8, 4))
    
    #The date variables have to be modified in order to be used in the filename (we're going to save it to the directory corresponding to the station name that we created way back at the start) because Windows quite sensibly won't allow filenames with /.  We could have avoided the use of slashes in the dates entirely, of course, but the .csv files came in that format, and frankly that's just how Americans write the date - I prefer '24.XII.2021' for Christmas Eve, e.g., myself, but I'm just a voice in the wilderness...
    start = start.replace('/', '.')
    end = end.replace('/', '.')

    #Retrieve the figure we created above in order to save it; I frankly can't remember why it has to be done this way, but I believe that it does, at least if you don't want the figure to be displayed first, which I don't - I find that the display area in the console is too small for convenient viewing, and that the display of the plots clutters the display and distracts the user from the efficient retrieval of the plots.  My program saves all the plots to directories created for the purpose, to be viewed and compared later.  They're intuitively named, and the program informs the user of the save locations upon successful export as well.
    fig = var_stat_plot.get_figure()
    #The filepath for saving uses the df_name_chosen variable to get into the final directory, then creates a unique name for the plot using the station name, variable plotted, and date range used.  If someone entered the same variables (station, plot variable, and dates), the plot would be overwritten, but only with the exact same plot, so, no harm done.
    fig.savefig('fa21python2_adam/Final_Project/Plots/Single_Stations/'+df_name_chosen+'/'+df_fixed_name+'_'+print_variable+'_'+start+'-'+end+'.jpg')
    #Closing the plot for prudence's sake, and RAM too, I suppose.
    plt.close(fig)
    print('\nPlot successfully exported to \'Plots/Single_Stations/'+df_name_chosen+'\'')   

#This function graphs the mean for each weather variable for each station for the specified date range, and also averages the average for all stations, graphing that as well.
def descriptive_stats_grapher():
    
    #I'm going to stop describing code that's already been addressed from here on out.
    df_dict, start, end = slice_dfs()
    
    #turn the keys of the df_dict into a list that we can iterate over; don't necessarily have to cast it as a list, but seems a bit safer...
    df_keys =list(df_dict.keys())
    
    #This iterates over the whole dictionary of dataframes and replaces each with the (vastly smaller) dataframe that one gets from calling the df.describe() function; this returns means, standard deviations, counts, and the like.
    for key in df_keys:
        df_dict[key] = df_dict[key].describe()

    #For now, I don't care about anything in the described dfs other than the means for each weather variable, so I'm going to redefine each value in the df_dict(ionary) as the Pandas Series we get when we use .loc['mean']; just to reiterate, what we now have in df_dict is a dictionary in which the keys are the station names (14 as of the time of writing) and the values are now just a series of 4 numbers, each the mean of a different weather variable (Snowfall, Snowdepth, TempMin and TempMax).
    for key in df_keys:
        df_dict[key] = pd.Series(df_dict[key].loc['mean'])
    
    #Drop null values from the series in our dictionary    
    for key in df_keys:
        df_dict[key] = df_dict[key].dropna()
        #If dropping nulls results in an empty series, then we get rid of that key/value pair entirely; not doing so would create problems later, especially in our calculation of the average of all stations.
        if df_dict[key].empty is True:
            del df_dict[key]
    
    #Same exact code as above, but we have to run it again to exclude the entries that may have been deleted when we dropped all our empty series.    
    df_keys = list(df_dict.keys())
        
    #Now we make a new set of four dictionaries, one for each weather variable; each will be loaded up with one key/value pair for each station left in df_keys, the key being the station name and the value just being a number, whatever the mean for that weather variable at that station was.
    snowfall_dict = {}
    snowdepth_dict = {}
    tempmin_dict = {}
    tempmax_dict = {}
    
    #Load them dictionaries up!
    for key in df_keys:
        if key in df_dict:
            snowfall_dict[key] = df_dict[key].loc['Snowfall']
        snowdepth_dict[key] = df_dict[key].loc['Snowdepth']
        tempmin_dict[key] = df_dict[key].loc['TempMin']      
        tempmax_dict[key] = df_dict[key].loc['TempMax']  
        
    '''for key in df_keys:
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
                df_keys.remove(key)'''
        
    for key in df_keys:
        snowfall_dict[key] = float(snowfall_dict[key])
        snowdepth_dict[key] = float(snowdepth_dict[key])
        tempmin_dict[key] = float(tempmin_dict[key])
        tempmax_dict[key] = float(tempmax_dict[key])    
    
    av_var_choice = input('Pick a variable and to see the graph of its average for each station.  Note that some stations\' reporting period is longer or shorter than others, and each station\'s records may have gaps, so a comparison of means may be unequal. If a station does not appear in the plot, that means that there was no data for that station during the specified time frame.\n\n1. Average Daily Snowfall\n2. Average Daily Snow Depth\n3. Average Daily Minimum Temperature\n4. Average Daily Maximum Temperature\n\nChoice: ')
    
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
        
    else:
        print('\nInput not recognized.  Returning to menu.')
   
                
def comparison_plotter():
     
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
                  
    df_columns = list(all_stations_df.columns)
    remove_me = df_columns[0]
    fix_me = df_columns[1]
    fixed_me = fix_me.rstrip('_y')
    
    all_stations_df.drop(remove_me, axis=1, inplace=True)

    all_stations_df.rename(columns={fix_me:fixed_me}, inplace=True)
        
    all_stations_df = all_stations_df.reset_index()
    all_stations_df['ObDate'] = pd.to_datetime(all_stations_df['ObDate'])
    all_stations_df = all_stations_df.set_index('ObDate')
    all_stations_df = all_stations_df.sort_index()
    
    ob_count = str(len(all_stations_df.index))
    
    start = start.replace('/', '.')
    end = end.replace('/', '.')

    summary_stats = all_stations_df.describe()
    summary_stats.to_csv('fa21python2_adam/Final_Project/Summary_Stats_'+var_sel+'.csv')
    all_stations_plot = all_stations_df.plot(title='Historical '+fixed_var_sels[var_sel], xlabel='Observations = '+ob_count, ylabel=fixed_var_sels[var_sel]+unit, style='.', ms=12, figsize = (25, 10))
    
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
    y_choice = input('Choose a variable to plot on the y axis: \n\n1.Mean Daily Snowfall\n2.Mean Daily Snow Depth\n3.Mean Daily Minimum Temperature\n4.Mean Daily Maximum Temperature\n\nChoice: ')
    
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
        x_chosen = 'Weighted Average for Latitude and Elevation (Z-score)'
    
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
    
    station_list = ['Erie', 'Dubois', 'Indiana', 'Laurel Mountain', 'New Castle', 'Pittsburgh', 'Tionesta', 'Uniontown', 'Warren', 'Waynesburg']
    
    menu_choice = input('1. Pick date range (last used is default)\n2. Plot Precipitation and Snowfall Variables for a single station\n3. Compare averages across stations\n4. Compare a variable across all stations\n5. Plot correlations between station location and temperature and precipitation \n6. View list of stations\n7. Show current start and end dates\n8. Quit (Q/q)\n\nChoice: ')
    
    menu_choices = ['1', '2', '3', '4', '5', '6', '7', '8']
    
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
            print(station_list)
            menu()
        if menu_choice == '7':
            show_slicer_dates()
            menu()
        if menu_choice == '8':
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