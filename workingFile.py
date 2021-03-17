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
df = pd.read_csv("C:\\Users\\Jun Hso\\Desktop\\JHprac_coordinates.csv")

print(df['Current Timestamp'].apply(format_time))
