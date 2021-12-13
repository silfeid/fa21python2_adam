# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:45:24 2021

@author: brode
"""

import os

def analyze_file_list(dirname, filelist):
    
    for fl in filelist:
        filepath = dirname + str(os.sep) + fl
        print('File at: ', +filepath)
        
        try:
            if os.path.isfile(filepath):
                print(os.path.getsize(filepath)
                      
        except OSError:
            print('Error at: ', filepath)