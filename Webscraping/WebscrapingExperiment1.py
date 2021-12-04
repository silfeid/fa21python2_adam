# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:23:06 2021

@author: brode
"""
import re 

x = "This is a sentence (indeed) flarble [13]garble.[2]"

x = re.sub("[\[].*?[\]]", "", x)

print(x)
