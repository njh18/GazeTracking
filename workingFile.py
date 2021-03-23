# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

import pandas as pd
from datetime import datetime,timedelta
from itertools import islice
import os
import random


def format_time(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        # manually round up
        t = t + datetime.timedelta(milliseconds=1)
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def calcTimeDiff(dateobject1,dateobject2):
  timeDiff = dateobject1-dateobject2
  timeDiffMs = timeDiff.total_seconds()*1000
  return timeDiffMs


# get csv files
coordDf = pd.read_csv("C:\\Users\\ngjun\\Documents\\GitHub\\GazeTracking\\Data\\JHprac\\JHprac_coordinates.csv")
sheet_to_df_map = pd.read_excel("C:\\Users\\ngjun\\Documents\\GitHub\\GazeTracking\\Data\\JHprac\\JHprac_Sensors\\compiled_sensors.xlsx", sheet_name=None)

#Getting sheetnames
mylist = sheet_to_df_map.keys()


# append names into column
columnNames = []
for sheet in mylist:
    currentColumns = list(sheet_to_df_map[sheet].columns)
    for columnName in currentColumns:
        if columnName not in ('Unnamed: 0', 'time', 'seconds_elapsed','timestamp'):
            columnNames.append(sheet+"_"+columnName)

# Convert all timestamp values to datetime
for currentSheet in mylist:
    sheet_to_df_map[currentSheet]['timestamp'] = pd.to_datetime(sheet_to_df_map[currentSheet]['timestamp'], format='%Y-%m-%d %H:%M:%S.%f')
coordDf['Current Timestamp'] = pd.to_datetime(coordDf['Current Timestamp'],format = '%Y-%m-%d %H:%M:%S.%f')
print("Converted timestamps to datetime")

############################################## MAIN CODE #########################################

for currentSheet in mylist:
    print(currentSheet)
    #get names of columns to be added into coordDf
    currentColumns = list(sheet_to_df_map[currentSheet].columns)
    toremove =['Unnamed: 0', 'time', 'seconds_elapsed','timestamp']
    for name in toremove:
        currentColumns.remove(name)
    print(currentColumns)

    #Barometer and light have different 
    if currentSheet in ['Barometer','Light']:
        timestamps = []
        for index, row in islice(sheet_to_df_map[currentSheet].iterrows(),0,None):
            if index < len(sheet_to_df_map[currentSheet].index)-1:
                timestamps.append((index,row['timestamp'],sheet_to_df_map[currentSheet].iloc[index+1]['timestamp'])) 
        print("Timestamp list done")
        start = 0
        for index, row in islice(coordDf.iterrows(),0,None):
            ### For checking progress
            if index%100 == 0:
                print("Current index is %d" %(index))
                
            for i in range(start,len(timestamps)):
                if (timestamps[i][1] < row['Current Timestamp'] < timestamps[i][2]):
                    A = row['Current Timestamp'] - timestamps[i][1]
                    B = timestamps[i][2] - row['Current Timestamp']
                    if (A<B):
                        final = timestamps[i][0]
                    else:
                        final = timestamps[i][0]+1
                    start = i
                    break
                else:
                    continue
            for name in currentColumns:
              coordDf.loc[index, currentSheet+"_"+name] = sheet_to_df_map[currentSheet].iloc[final][name] 
    else:
        start = 0
        for index, row in islice(coordDf.iterrows(),0,None):
            ### For checking progress
            if index%100 == 0:
                print("Current index is %d" %(index))
            suitablevalues = []
            for index1, row1 in islice(sheet_to_df_map[currentSheet].iterrows(), start, None):
                # Retrieving the time difference in ms betwen sensor and video timestamp
                timediff = calcTimeDiff(row['Current Timestamp'],row1['timestamp'])
                # Checking for values that have timediff within 33 ms
                if timediff > 33:
                    continue
                elif -33 <= timediff <= 33:
                    suitablevalues.append((index1,row1['timestamp'],abs(timediff))) 
                else:
                    start = index1
                    break
        
            #Choosing the timestamp that has the minimal difference between sensor and video
            final = min(suitablevalues, key = lambda x: x[2])
        
            for name in currentColumns:
              coordDf.loc[index, currentSheet+"_"+name] = sheet_to_df_map[currentSheet].iloc[final[0]][name]


print(coordDf.head())

coordDf.to_csv("JHprac_Compiled.csv")