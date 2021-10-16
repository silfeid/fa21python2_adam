# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:03:45 2021

@author: brode
"""

import csv
import sys


def func_quit():
    sys.exit()


def intro():
    quit_commands = ['Q', 'q']

    print('Welcome to the icon project.  I can read in any 10x10 csv file of 0s and 1s and print the design thus represented as an icon.  I can also scale the icon up in size 2x, 3x or 4x, rotate it to the left or right, mirror it, and invert it.  Well, hopefully, anyway!')

    user_command = input('Press any key to proceed, or type Q or q to quit: ')

    if user_command not in quit_commands:
        print('\nHere we go!')

    if user_command in quit_commands:
        func_quit()


def solicit_filepath():

    filepath_text = input(
        'Type a filepath (relative or absolute) to feed your own csv file into the icon transformer, otherwise hit enter to proceed with the default icon: ')

    if filepath_text == '':
        filepath_text = 'fa21python2_adam\\Icon_Project\\Icon_Design.csv'

    else:
        filepath_text = filepath_text

    with open('fa21python2_adam\\Icon_Project\\filepath.txt', 'w') as filepath_object:
        filepath_object.write(filepath_text)
        filepath_object.close()


def menu_select():

    valid_user_choices = ['1', '2', '3', '4', '5', '6', 'Q', 'q']

    user_choice = input('Type the number corresponding to the option you would like to pursue, or Q/q to quit.\n\n1.Scale the icon up.\n2.Scale the icon down.\n3.Mirror the icon.\n4.Invert the Icon.\n5.Rotate the icon 90 degrees left or right.\n6.Print the icon.\n\nInput: ')

    if user_choice in valid_user_choices:

        if user_choice == '1':
            scale_up_icon()
            menu_select()

        if user_choice == '2':
            scale_down_icon()
            menu_select()

        if user_choice == '3':
            mirror_icon()
            menu_select()

        if user_choice == '4':
            invert_icon()
            menu_select()

        if user_choice == '5':
            rotate_icon()
            menu_select()

        if user_choice == '6':
            print_icon()
            menu_select()

        if user_choice == 'q' or user_choice == 'Q':
            print('\nBye!')
            func_quit()

    else:
        menu_select()


def grab_filepath():

    with open('fa21python2_adam\\Icon_Project\\filepath.txt', 'r') as filepath_object:
        filepath_text = filepath_object.read()
    return filepath_text


def read_in_icon():

    filepath_text = grab_filepath()
    icon_dict = {}
    icon_dict_key = 0

    with open(filepath_text, 'r') as temp_file:
        reader = csv.reader(temp_file)
        # Need input controls here, apparently...maximum row length for csv, input must be 0s and 1s only...
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
    return icon_dict


def print_icon():

    icon_dict = read_in_icon()
    key_to_read = 0

    print()

    for key in icon_dict:
        key_to_read += 1

        print_line = (icon_dict[key_to_read])

        print_string = ''.join(print_line)

        corr_print_string = print_string.replace('0', '  ')

        corr_print_string = corr_print_string.replace('1', '**')

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

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')

    if len(value_list[0]) == 10:
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

    for value in icon_dict.values():
        default_string = default_string+''
        for item in value:
            default_string = default_string+item

        default_string = default_string+','

    default_string = default_string.rstrip(',')
    value_list = default_string.split(',')
    
    clockwise = [''.join(col)[::-1] for col in zip(*value_list)]
    print(clockwise)

    write_csv(clockwise)

def write_csv(icon_list):

    filepath_text = grab_filepath()

    with open(filepath_text, 'w', newline='') as icon_list_object:
        icon_list_file = csv.writer(icon_list_object)
        icon_list_file.writerows(icon_list)

    icon_list_object.close()


def main():
    intro()
    solicit_filepath()
    menu_select()


if __name__ == "__main__":
    main()
