# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:16:45 2021

@author: brode
"""

import sqlite3

dbconn = sqlite3.connect('recall.db')

cursor = dbconn.cursor()

try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                       vehicle (
                           vehid INTEGER PRIMARY KEY,
                           model TEXT NOT NULL,
                           year  INTEGER,
                           recallcount INTEGER
                           )''')
    dbconn.commit()

except sqlite3.Error as er:
    print('Execute error: ' + er)
    
table = cursor.execute('SELECT * FROM vehicle')
print(table)