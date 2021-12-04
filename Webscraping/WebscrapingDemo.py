# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:23:06 2021

@author: brode
"""

from bs4 import BeautifulSoup

#Get raw html text from page
#this demo is of local page, but can use requests.get() to grab html from any networked webserver on the planet!

html_soup = None

with open('fa21python2_adam/Webscraping/webpage.html') as webpage:
    #Verify that you have raw html

    soup = BeautifulSoup(webpage.read(), 'html.parser')
    #Here, the soup.p returns all elements from soup that have the <p> "text" </p> tag identifying them; can do this with any of the tags (h1, h2, li, etc.)
    print(soup.p)
    #Get text only from that tag:
    print('\n'+soup.p.text)
    #Grab all list items with class 
    glarbin = (soup.find_all('li'))
    print()
    for flarbin in glarbin:
        print(flarbin.text)
    
    