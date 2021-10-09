# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:25:50 2021

@author: brode
"""
import csv

def read_in_icon():
    
    icon_dict = {}
    icon_dict_key = 0
    
    with open('fa21python2_adam\\ICON Design - Sheet1.csv', 'r') as temp_file:
        reader = csv.reader(temp_file)
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

                
def main():
    print_icon()

    
if __name__ == "__main__":
    main()