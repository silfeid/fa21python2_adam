# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:25:50 2021

@author: brode
"""
import csv
#GOTTA ADD CODING COMMNTARY - DOCSTRINGS!!!

def read_in_icon():
    
    icon_dict = {}
    icon_dict_key = 0
    
    with open('fa21python2_adam\\Icon_Project\\Icon_Design.csv', 'r') as temp_file:
        reader = csv.reader(temp_file)
        #Need input controls here, apparently...maximum row length for csv, input must be 0s and 1s only...
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
            
    return icon_dict

def read_in_scaled_icon():
    
    icon_dict = {}
    icon_dict_key = 0
    
    with open('fa21python2_adam\\Icon_Project\\scaled_icon.csv', 'r') as temp_file:
        reader = csv.reader(temp_file)
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
            
    return icon_dict

def read_in_inverted_icon():
    
    icon_dict = {}
    icon_dict_key = 0
    
    with open('fa21python2_adam\\Icon_Project\\inverted_icon.csv', 'r') as temp_file:
        reader = csv.reader(temp_file)
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
            
    return icon_dict

def read_in_mirrored_icon():
    
    icon_dict = {}
    icon_dict_key = 0
    
    with open('fa21python2_adam\\Icon_Project\\mirrored_icon.csv', 'r') as temp_file:
        reader = csv.reader(temp_file)
        for line in reader:
            icon_dict_key += 1
            icon_dict[icon_dict_key] = line
            
    return icon_dict

def print_icon():
    
    icon_dict = read_in_icon()
    key_to_read = 0
    
    print()
    print('ORIGINAL\n')
    
    for key in icon_dict:
        key_to_read += 1
        
        print_line = (icon_dict[key_to_read])
        
        print_string = ''.join(print_line)
        
        corr_print_string = print_string.replace('0', '  ')
        
        corr_print_string = corr_print_string.replace('1', '**')  
        
        print(corr_print_string)
    
    print()
        
def print_scaled_icon():
    
    icon_dict = read_in_scaled_icon()
    key_to_read = 0
    
    print()
    print('SCALED x2\n') 
    
    for key in icon_dict:
        key_to_read += 1
        
        print_line = (icon_dict[key_to_read])
        
        print_string = ''.join(print_line)
        
        corr_print_string = print_string.replace('0', '  ')
        
        corr_print_string = corr_print_string.replace('1', '**')  
        
        print(corr_print_string)
    
    print()
    
def print_inverted_icon():
    
    icon_dict = read_in_inverted_icon()
    key_to_read = 0
    
    print()
    print('INVERTED\n')
    
    for key in icon_dict:
        key_to_read += 1
        
        print_line = (icon_dict[key_to_read])
        
        print_string = ''.join(print_line)
        
        corr_print_string = print_string.replace('0', '  ')
        
        corr_print_string = corr_print_string.replace('1', '**')  
        
        print(corr_print_string)
    
    print()

def print_mirrored_icon():
    
    icon_dict = read_in_mirrored_icon()
    key_to_read = 0
    
    print()
    print('MIRRORED\n')
    
    for key in icon_dict:
        key_to_read += 1
        
        print_line = (icon_dict[key_to_read])
        
        print_string = ''.join(print_line)
        
        corr_print_string = print_string.replace('0', '  ')
        
        corr_print_string = corr_print_string.replace('1', '**')  
        
        print(corr_print_string)
    
    print()

def scale_icon():
    
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
        
    return scaled_list

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
    
    return inverted_list

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
    
    return mirrored_list

def write_scaled_csv():
    
    scaled_list = scale_icon()
    
    with open('fa21python2_adam\\Icon_Project\\scaled_icon.csv', 'w', newline = '') as scaled_list_object:
        scaled_list_file = csv.writer(scaled_list_object)
        scaled_list_file.writerows(scaled_list)
        
    scaled_list_object.close()
    
def write_mirrored_csv():
    
    mirrored_list = mirror_icon()
    
    with open('fa21python2_adam\\Icon_Project\\mirrored_icon.csv', 'w', newline = '') as mirrored_list_object:
        mirrored_list_file = csv.writer(mirrored_list_object)
        mirrored_list_file.writerows(mirrored_list)
        
    mirrored_list_object.close()
    
def write_inverted_csv():
    
    inverted_list = invert_icon()
    
    with open('fa21python2_adam\\Icon_Project\\inverted_icon.csv', 'w', newline = '') as inverted_list_object:
        inverted_list_file = csv.writer(inverted_list_object)
        inverted_list_file.writerows(inverted_list)
        
    inverted_list_object.close()
                
def main():
    print_icon()
    write_scaled_csv()
    print_scaled_icon()
    write_inverted_csv()
    print_inverted_icon()
    write_mirrored_csv()
    print_mirrored_icon()
    
if __name__ == "__main__":
    main()