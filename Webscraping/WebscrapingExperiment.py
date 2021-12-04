# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:23:06 2021

@author: brode
"""

from bs4 import BeautifulSoup
import requests
import re

filepath = 'fa21python2_adam/Webscraping/WikiPages/'

page = input('Type a Wikipedia page; no input validation, so choose wisely: ')

wikipage = 'https://en.wikipedia.org/wiki/'+page

r = requests.get("{}".format(wikipage))
data = r.text
soup = BeautifulSoup(data, 'lxml', from_encoding='utf8')

glarbin = soup.find('h1')
glarbin = glarbin.text

flarbin = soup.find_all('p')

full_filepath = filepath+page+'.txt'

with open(full_filepath, 'w') as title_page:
    title_page.write(glarbin)
    title_page.close()

for item in flarbin:
    item = item.get_text()
    if not item:
        pass
    else:
        item = re.sub("[\[].*?[\]]", "", item)
        with open(full_filepath, 'a', encoding='utf-8') as page:
            page.write(item)
            page.write('\n')
    
page.close()

print('\nWikipedia page saved as:'+full_filepath)