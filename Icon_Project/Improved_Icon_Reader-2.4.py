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

def choose_char():
    valid_char_choices = ['*', '#', '@', '$']

    char_choice = input('Choose from *, #, @, or $ as the fill-unit with which to draw your icon by typing the character of your choice: ')
    if char_choice in valid_char_choices:
        with open('fa21python2_adam\\Icon_Project\\Icon_Files\\charchoice.txt', 'w') as char_doc:
            char_doc.write(char_choice)
    else:
        choose_char()
        
def grab_char():
    
    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\charchoice.txt', 'r') as char_doc:
        char = char_doc.read()
    return char

def write_csv(icon_list):

    filepath_text = grab_filepath()
    
    if 'tempfile' in filepath_text:
        filepath_text = filepath_text
    else:
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Files\\tempfile.csv'

    with open(filepath_text, 'w', newline='') as icon_list_object:
        icon_list_file = csv.writer(icon_list_object)
        icon_list_file.writerows(icon_list)

    icon_list_object.close()
    
    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\filepath.txt', 'w') as filepath_object:
        filepath_object.write(filepath_text)
        filepath_object.close()

def save_icon():
    
    filepath_text = grab_filepath()
    icon_dict = {}
    icon_dict_key = 0
    default_string = ''
        
    with open(filepath_text, 'r') as temp_file:
        reader = csv.reader(temp_file)
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
            
    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')

    save_over_yes = ['Y', 'y']
    save_name = input('Enter the name for the icon file to be saved (.csv) - file extension not required.  File will be saved at fa21python2_adam\\Icon_Project\\Icon_Files\...')
    save_name = 'fa21python2_adam\\Icon_Project\\Icon_Files\\' + save_name + '.csv'
    
    if os.path.exists(save_name) is True:
        save_over = input('That filepath already exists.  Are you sure you want to overwrite the existing file? Y/N: ')
        if save_over in save_over_yes:
            with open(save_name, 'w', newline='') as icon_list_object:
                icon_list_file = csv.writer(icon_list_object)
                icon_list_file.writerows(value_list)
            print('\nFile saved successfully!')
        else:
            save_icon()

    if os.path.exists(save_name) is False:

        with open(save_name, 'w', newline='') as icon_list_object:
            icon_list_file = csv.writer(icon_list_object)
            icon_list_file.writerows(value_list)
    
        icon_list_object.close()
    
        print('\nFile saved successfully!')
    menu_select()


def init_read_in():
    
    icon_dict = read_in_icon()
    default_string = ''
    valid_chars = ['0', '1']
    invalid_count = 0
    item_count = 0

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')
    
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
        print('\n********Icon format is invalid - only 0\'s and 1\'s accepted.  Please revise or try another design.********')
        solicit_filepath()
    else:

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

    user_command = input('Press any key to proceed, or type Q or q to quit: ')

    if user_command not in quit_commands:
        print('\nHere we go!')

    if user_command in quit_commands:
        func_quit()

def solicit_filepath():

    filepath_text = input(
        'Type the name of a CSV file (without extension) in the Icon_Project\\Icon_Files Folder to feed your own csv file into the icon transformer, otherwise hit enter to proceed with the default icon: ')

    if filepath_text == '':
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Files\\Icon_Design.csv'

    else:
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Files\\'+filepath_text+'.csv'

    with open('fa21python2_adam\\Icon_Project\\Icon_Files\\filepath.txt', 'w') as filepath_object:
        filepath_object.write(filepath_text)
        filepath_object.close()
        
    init_read_in()

def menu_select():

    valid_user_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'q']

    user_choice = input('Type the number corresponding to the option you would like to pursue, or Q/q to quit.\n\n1.Print the icon.\n2.Scale the icon up.\n3.Scale the icon down.\n4.Mirror the icon.\n5.Invert the Icon.\n6.Rotate the icon 90 degrees left or right.\n7.Change the print character.\n8.Change the icon.\n9.Save the icon.\n\nInput: ')

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
            init_read_in()
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
        print('\nGreat! That worked.  Let\'s proceed.')
    
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
        print('\nItem too small to be scaled down further.')
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
    
    rotation_dir = input('Type L/l to rotate the icon 90 degrees to the left (counter-clockwise) or R/r to rotate the icon 90 degrees to the right (clockwise), or type Q/q to return to the main menu: ')
    
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
