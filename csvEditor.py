# -*- coding: utf-8 -*-
"""
Combines sensor data from multiple csv files into 1 excel file with timestamp in timezone GMT +08
"""

import os
import pandas as pd
import datetime
import numpy as np


def format_time(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        t = t + datetime.timedelta(milliseconds=1)  # manually round up
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


# Change directory to datasets to get data
os.chdir("E:\\DATA_COMPLETED\\Sensor Logger\\")
coordinates = os.listdir()
coordinates.remove("Complete")
current_directory = os.getcwd()


for name in coordinates:
    index = name.find("-")
    user = name[:index]
    print("------- Current User is %s -------" % (user))
    os.chdir("D:\\DATA_COMPLETED\\Sensor Logger\\"+name+"\\")
    names = os.listdir()
    try:
        names.remove("Metadata.csv")
    except:
        pass
    try:
        names.remove("Microphone.m4a")
    except:
        pass

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter("C:\\Users\\ngjun\\Desktop\\Compiled Sensors\\" +
                            user + '_compiled_sensors.xlsx', engine='xlsxwriter')

    # print(list_of_names[0][-4:])
    for sheet in names:
        if sheet[-4:] == ".txt":
            pass
        else:
            try:
                df = pd.read_csv(sheet)

                # Change to datetime64[ns]
                df['timestamp'] = pd.to_datetime(df['time'], unit='ns')

                # Change to gmt +8
                df['timestamp'] = df['timestamp'] + pd.Timedelta('8 hour')

                # Convert into string
                df['timestamp'] = df['timestamp'].apply(format_time)

                df.to_excel(writer, sheet_name=sheet[:-4])

            except:
                pass

    writer.save()
    print("------- Completed %s -------" % (user))
