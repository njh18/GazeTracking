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
os.chdir("C:\\Users\\ngjun\\Desktop\\FINAL COMPILATION\\Ryan-2021-02-24_23-30-47\\")
current_directory = os.getcwd()


def format_time(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        t = t + datetime.timedelta(milliseconds=1)  # manually round up
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


names = os.listdir()
names.remove("Metadata.csv")

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('compiled_sensors.xlsx', engine='xlsxwriter')

# print(list_of_names[0][-4:])
for sheet in names:
    if sheet[-4:] == ".txt":
        pass
    else:
        df = pd.read_csv(sheet)

        # Change to datetime64[ns]
        df['timestamp'] = pd.to_datetime(df['time'], unit='ns')

        # Change to gmt +8
        df['timestamp'] = df['timestamp'] + pd.Timedelta('8 hour')

        # Convert into string
        df['timestamp'] = df['timestamp'].apply(format_time)

        print(df)

        df.to_excel(writer, sheet_name=sheet[:-4])

writer.save()
