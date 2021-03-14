# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:01:01 2021

@author: Jun Hso
"""

import os
import pandas as pd
import datetime
import numpy as np

# Change directory to datasets to get data
os.chdir("C:\\Users\\Jun Hso\\Documents\\GitHub\\GazeTracking\\Data\\JHPrac\\JHprac_Sensors")
current_directory = os.getcwd()


list_of_names = os.listdir()

print(list_of_names)

df = pd.read_csv(list_of_names[0])




#Change to datetime64[ns]
df['time'] = pd.to_datetime(df['time'], unit='ns')

#Change to gmt +8
df['time'] = df['time'] + pd.Timedelta('8 hour')

time=df['time'][0]
print(time)

def format_time(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        t = t + datetime.timedelta(milliseconds=1)  # manually round up
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]



df['time'] = df['time'].apply(format_time)

print(df['time'].head())
print(df['time'][0])

