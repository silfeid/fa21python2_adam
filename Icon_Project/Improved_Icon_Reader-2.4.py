# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:03:45 2021

@author: brode
"""

import csv
import sys
import os
import os.path

def func_quit():
    sys.exit()
#Grabbed how to do this from the internet - run this function when user input equals 'Q' or 'q' at certain points.  Seems pretty handy.

def choose_char():
    #This function allows the user to select which character they wish to use to draw their icon.  The symbol set is needed since these aren't covered by the built-in isalnum() function.  If the user picks a sumbol that isn't listed here and isn't a number or letter, the function rejects the input and runs afresh.  If a valid choice is made, the character is written to a text file, to be retrieved by the grab_char() function and then used in the print_icon() function.
    symbol_set = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '-', '_', '=', '+']
    char_choice = input('Type the character (symbol or alphanumeric) of your choice with which to draw your icon: ')
    if char_choice.isalnum() is True:
        with open('fa21python2_adam\\Icon_Project\\Icon_Files\\charchoice.txt', 'w') as char_doc:
            char_doc.write(char_choice)
    elif char_choice in symbol_set:
        with open('fa21python2_adam\\Icon_Project\\Icon_Files\\charchoice.txt', 'w') as char_doc:
            char_doc.write(char_choice)
    else:
        print('\nInvalid character, pick another.')
        choose_char()
        
def grab_char():
    #Opens the txt file from choose_char and retrieves the specific character/numeral/symbol chosen by the user.  Returns their choice (read from file) as variable 'char'.
    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\charchoice.txt', 'r') as char_doc:
        char = char_doc.read()
    return char

def write_csv(icon_list):
    #A pretty important function for this program.  Whatever transformations to the icon the user undertakes are saved as a csv file in the same format of 0's and 1's in which it was initially read in, though it can be (much) larger than the original file in terms of numbers of rows and columns.

    filepath_text = grab_filepath()
    #Retrieves the filepath for this particular icon (cf. def grab_filepath() for more info).
    if 'tempfile' in filepath_text:
        filepath_text = filepath_text
        #While it's being transformed, the icon design is saved as tempfile.csv; users have the option to save it permanently under a name of their choice(cf. def save_icon() for more info).  If this is the second or later transformation, the icon design will already be saved as tempfile, so the name doesn't need to be changed - it already is tempfile.
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Files\\tempfile.csv'
        #If this is the first transformation to the icon, it needs to be saved as tempfile.csv for the first time - executed here.

    with open(filepath_text, 'w', newline='') as icon_list_object:
        icon_list_file = csv.writer(icon_list_object)
        icon_list_file.writerows(icon_list)
        icon_list_object.close()
        #Create a new .csv file and write the icon_list (a list of the rows of the design) to a csv file.

    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\filepath.txt', 'w') as filepath_object:
        filepath_object.write(filepath_text)
        filepath_object.close()
        #Updates the name written in the filepath document to whatever it was changed to here; either from its original name to tempfile, or from tempfile to tempfile (no change)

def save_icon():
    #The function to (permanently) save the icon under a name of the user's choice in the Icon_Files folder.
    filepath_text = grab_filepath()
    icon_dict = {}
    icon_dict_key = 0
    default_string = ''
        
    with open(filepath_text, 'r') as temp_file:
        reader = csv.reader(temp_file)
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
     #Read the icon in        
            
    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item
    

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')
    #Convert the icon_dict to a list of strings (0's and 1's) that can easily be written to csv

    save_over_yes = ['Y', 'y']
    save_name = input('Enter the name for the icon file to be saved (.csv) - file extension not required.  File will be saved at fa21python2_adam\\Icon_Project\\Icon_Files\...')
    save_name = 'fa21python2_adam\\Icon_Project\\Icon_Files\\' + save_name + '.csv'
    #Variables need for user to enter their own file name; if they want to overwrite an existing file, what they want the new name to be, and then the filepath with directories and the file extension to format the filepath properly.  Should add input validation for disallowed characters...
    
    if os.path.exists(save_name) is True:
        save_over = input('That filepath already exists.  Are you sure you want to overwrite the existing file? Y/N: ')
        if save_over in save_over_yes:
            with open(save_name, 'w', newline='') as icon_list_object:
                icon_list_file = csv.writer(icon_list_object)
                icon_list_file.writerows(value_list)
            print('\nFile saved successfully!')
        else:
            save_icon()
    #Script for overwrite, using the exists function imported from os.path (pretty handy) to check if the file already exists or not and prompt the user accordingly (below also).

    if os.path.exists(save_name) is False:

        with open(save_name, 'w', newline='') as icon_list_object:
            icon_list_file = csv.writer(icon_list_object)
            icon_list_file.writerows(value_list)
    
        icon_list_object.close()
    
        print('\nFile saved successfully!')
    menu_select()
    #Return the user to the main menu once the file saving is completed.

def init_read_in():
    #It's a bit clunky that there are two read_in functions, but since the user isn't supposed to be able to reduce the icon to a size smaller than its original one (I can't control distortions or the cutting-off of parts of the image if they do), I need to use this function to track its original size in order to inhibit the scale_down_icon() function from shrinking the icon below its original size.
    
    icon_dict = read_in_icon()
    #So we just use the normal read_in_icon() function to get the design, making sure that we run the init_read_in() function before running any transformations.
    default_string = ''
    valid_chars = ['0', '1']
    invalid_count = 0
    item_count = 0
    #These variables will be used below to check the csv file for correct formatting

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')
    
    #Converting the design to the list format (strings of 0's and 1's) that is equivalent to the csv file;
    
    for item in value_list:
        for char in item:
            if char not in valid_chars:
                invalid_count += 1
            else:
                invalid_count += 0
        item_count += 1
                
        if len(item) > 40:
            invalid_count += 1
        if item_count > 40:
            invalid_count += 1
        
    if invalid_count > 0:
        print('\nIcon format is invalid!\nOnly 0\'s and 1\'s accepted!\nMaximum row/column size of 40!\nPlease revise this design or try another.')
        solicit_filepath()
    else:
        print('\nOptional icon design loaded successfully.')
        
        row_count = len(value_list[0])
    
        with open('fa21python2_adam\\Icon_Project\\Icon_Files\\rowlength.txt', 'w') as rowlength:
            rowlength.write(str(row_count))
            rowlength.close()

def grab_row_count():
    
    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\rowlength.txt', 'r') as rowlength:
        row_count = int(rowlength.read())
   
    return row_count

def intro():
    quit_commands = ['Q', 'q']

    print('Welcome to the icon project.  I can read in a csv file of 0s and 1s comprised of up to approximately 40 rows/columns and print the design thus represented as an icon. I can also scale the icon up in size at intervals of 2x and back down (though no smaller than its original size), rotate it to the left or right, mirror it, and invert it.')

    user_command = input('Hit Enter to proceed, or type Q/q to quit: ')

    if user_command in quit_commands:
        func_quit()

def solicit_filepath():

    filepath_text = input(
        'Type the name of a CSV file (without extension) in the Icon_Project\\Icon_Files Folder to feed your own csv file into the icon transformer, otherwise hit enter to proceed with the default icon: ')

    if filepath_text == '':
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Files\\Icon_Design.csv'
        print('\nDefault icon loaded.')

    else:
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Files\\'+filepath_text+'.csv'
        

    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\filepath.txt', 'w') as filepath_object:
        filepath_object.write(filepath_text)
        filepath_object.close()
        
    init_read_in()

def menu_select():

    valid_user_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'q']

    user_choice = input('Type the number corresponding to the option you would like to pursue, or Q/q to quit.\n\n1.Print the icon\n2.Scale the icon up\n3.Scale the icon down\n4.Mirror the icon\n5.Invert the Icon\n6.Rotate the icon 90 degrees left or right\n7.Change the print character\n8.Change the icon\n9.Save the icon\n\nInput: ')

    if user_choice in valid_user_choices:

        if user_choice == '1':
            print_icon()
            menu_select()
            
        if user_choice == '2':
            scale_up_icon()
            menu_select()

        if user_choice == '3':
            scale_down_icon()
            menu_select()

        if user_choice == '4':
            mirror_icon()
            menu_select()

        if user_choice == '5':
            invert_icon()
            menu_select()

        if user_choice == '6':
            rotate_icon()
            menu_select()
            
        if user_choice == '7':
            choose_char()
            menu_select()

        if user_choice == '8':
            solicit_filepath()
            menu_select()
            
        if user_choice == '9':
            save_icon()
            menu_select()

        if user_choice == 'q' or user_choice == 'Q':
            print('\nBye!')
            func_quit()

    else:
        menu_select()

def grab_filepath():

    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\filepath.txt', 'r') as filepath_object:
        filepath_text = filepath_object.read()
    return filepath_text

def read_in_icon():

    filepath_text = grab_filepath()
    icon_dict = {}
    icon_dict_key = 0
    
    if os.path.exists(filepath_text) is True:
        
        with open(filepath_text, 'r') as temp_file:
            reader = csv.reader(temp_file)
            for line in reader:
                icon_dict_key += 1
                icon_dict[icon_dict_key] = line
    
    if os.path.exists(filepath_text) is False:
        print('\nThat filepath does not exist.  Try another.')
        solicit_filepath()
    
    return icon_dict

def print_icon():

    icon_dict = read_in_icon()
    char = grab_char()
    key_to_read = 0

    print()

    for key in icon_dict:
        key_to_read += 1

        print_line = (icon_dict[key_to_read])

        print_string = ''.join(print_line)

        corr_print_string = print_string.replace('0', '  ')

        corr_print_string = corr_print_string.replace('1', char+char)

        print(corr_print_string)

    print()

def scale_up_icon():

    icon_dict = read_in_icon()
    scaled_list = []
    default_string = ''

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')

    for item in value_list:
        item = item.replace('1', '11')
        item = item.replace('0', '00')
        scaled_list.append(item)
        scaled_list.append(item)

    write_csv(scaled_list)

def scale_down_icon():

    icon_dict = read_in_icon()
    scaled_list = []
    default_string = ''
    row_count = grab_row_count()
    
    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')

    if len(value_list[0]) <= row_count:
        print('\nItem too small to be scaled down any further (original size reached).')
        for item in value_list:
            scaled_list.append(item)

    else:

        for item in value_list:
            item = item.replace('11', '1')
            item = item.replace('00', '0')
            scaled_list.append(item)

        scaled_list = scaled_list[::2]

    write_csv(scaled_list)

def mirror_icon():

    icon_dict = read_in_icon()
    mirrored_list = []
    default_string = ''

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')

    for item in value_list:
        item = item[::-1]
        mirrored_list.append(item)

    write_csv(mirrored_list)

def invert_icon():

    icon_dict = read_in_icon()
    inverted_list = []
    default_string = ''

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')

    value_list.reverse()

    inverted_list = value_list

    write_csv(inverted_list)

def rotate_icon():

    icon_dict = read_in_icon()
    default_string = ''
    L_commands = ['L', 'l']
    R_commands = ['R', 'r']
    Q_commands = ['Q', 'q']
    
    rotation_dir = input('Type L/l to rotate the icon 90 degrees to the left (counter-clockwise), R/r to rotate the icon 90 degrees to the right (clockwise), or type Q/q to return to the main menu: ')
    
    if rotation_dir in L_commands:
        
        for value in icon_dict.values():
            default_string = default_string+''
            for item in value:
                default_string = default_string+item
        
            default_string = default_string+','
    
        default_string = default_string.rstrip(',')
        value_list = default_string.split(',')
     
        counter_clockwise_list = [''.join(col) for col in zip(*value_list)][::-1]
        
        write_csv(counter_clockwise_list)
        menu_select()
        
    if rotation_dir in R_commands:
        
        for value in icon_dict.values():
            default_string = default_string+''
            for item in value:
                default_string = default_string+item
        
            default_string = default_string+','
    
        default_string = default_string.rstrip(',')
        value_list = default_string.split(',')
     
        clockwise_list = [''.join(col)[::-1] for col in zip(*value_list)]
    
        write_csv(clockwise_list)
        menu_select()
        
    if rotation_dir in Q_commands:
        menu_select()
        5
    else:
        rotate_icon()



def main():
    intro()
    solicit_filepath()
    grab_row_count()
    choose_char()
    menu_select()


if __name__ == "__main__":
    main()
