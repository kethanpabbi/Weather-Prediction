# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:53:08 2020

@author: kethanpabbi
"""
from wwo_hist import retrieve_hist_data
import os
os.chdir("/Users/kethanpabbi/Desktop/Minor Project/python")
frequency=3
start_date = '11-DEC-2018'
end_date = '30-JAN-2020'
api_key = 'fe488bebe919444e993200836200605'
location_list = ['Bengaluru']

hist_weather_data = retrieve_hist_data(api_key,
                                       location_list,
                                       start_date,end_date,frequency,
                                       location_label = False,
                                       export_csv = True,
                                       store_df = True)