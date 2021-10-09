# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:45:28 2021

@author: brode
"""


def results_dumper():
    if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json') is True:
        with open('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json') as old_query_object:
            old_query = old_query_object.read()
            old_query_object.close()
            old_query = json.loads(old_query)
    
            old_query.update(temp_query)
            updated_query = old_query
            
    if os.path.exists('C:\\Users\\brode\\Python\\fa21python2_adam\\query_resultse_data.json') is False:
            updated_query = temp_query
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\query_results_data.json', 'w') as jsonfile:
                json.dump(updated_query, jsonfile)
    
    
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\temperature_min_data.json') as temp_min_dict_object:
        temp_min_dict = temp_min_dict_object.read()
        temp_min_dict_object.close()
        temp_min_dict = json.loads(temp_min_dict)
        
    with open('C:\\Users\\brode\\Python\\fa21python2_adam\\snowdepth_data.json') as snowdepth_dict_object:
        snowdepth_dict = snowdepth_object.read()
        snowdepth_dict_object.close()
        snowdepth_dict = json.loads(snowdepth_dict)