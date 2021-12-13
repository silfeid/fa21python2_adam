# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:55:53 2021

@author: brode
"""

import os

#for loc, dirs, file in os.walk('fa21python2_adam'):
    #print('Location: ', loc)
    #print('Directories: ', dirs)
    #print('Files: ', file)
    #print('**********************')
          
    
def analyze_file_list(dirname, filelist):
    
    for fl in filelist:
        filepath = dirname + str(os.sep) + fl
        print('File at: ', + filepath)
        
        try:
            if os.path.isfile(filepath):
                print(os.path.getsize(filepath))
                      
        except OSError:
            print('Error at: ', filepath)
            

analyze_file_list(loc, file)

