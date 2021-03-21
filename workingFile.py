# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

import os
import pandas as pd
import datetime


def format_time(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        # manually round up
        t = t + datetime.datetime.timedelta(milliseconds=1)
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


# get directory
coordDf = pd.read_csv("C:\\Users\\Jun Hso\\Documents\\GitHub\\GazeTracking\\Data\\JHprac\\JHprac_coordinates.csv")

print(coordDf['Current Timestamp'].head)

# get rest of files
sheet_to_df_map = pd.read_excel("C:\\Users\\Jun Hso\\Documents\\GitHub\\GazeTracking\\Data\\JHprac\\JHprac_Sensors\\compiled_sensors.xlsx", sheet_name=None)

mylist = sheet_to_df_map.keys()
print(mylist)