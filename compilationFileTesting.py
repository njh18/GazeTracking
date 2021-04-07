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
import time


def calcTimeDiff(dateobject1,dateobject2):
  timeDiff = dateobject1-dateobject2
  timeDiffMs = timeDiff.total_seconds()*1000
  return timeDiffMs


# get csv files
coordDf = pd.read_csv("C:\\Users\\ngjun\\OneDrive\\Desktop\\FINAL COMPILATION\\Ryan_coordinates.csv",
                      dtype = {'Pin Code':str}, parse_dates=["Current Timestamp"] )

sheet_to_df_map = pd.read_excel("C:\\Users\\ngjun\\OneDrive\\Desktop\\FINAL COMPILATION\\Ryan-2021-02-24_23-30-47\\compiled_sensors.xlsx", 
                                sheet_name=None,parse_dates=["timestamp"] )

# Drop useless columns
coordDf = coordDf.drop(columns=["Video Timestamp","Time Passed",'Unnamed: 0'])

#Getting sheetnames
mylist = sheet_to_df_map.keys()

# append names into column
columnNames = []
for sheet in mylist:
    currentColumns = list(sheet_to_df_map[sheet].columns)
    for columnName in currentColumns:
        if columnName not in ('Unnamed: 0', 'time', 'seconds_elapsed','timestamp'):
            columnNames.append(sheet+"_"+columnName)

############################################## MAIN CODE #########################################

dflength = coordDf.shape[0]
for currentSheet in mylist:
    print(currentSheet)
    start_time = time.time()
    #get names of columns to be added into coordDf
    currentColumns = list(sheet_to_df_map[currentSheet].columns)
    toremove =['Unnamed: 0', 'time', 'seconds_elapsed','timestamp']
    for name in toremove:
        currentColumns.remove(name)
        

    #Barometer and light have different ways of combining df
    if currentSheet in ['Barometer','Light','location']:
        timestamps = []
        for index, row in islice(sheet_to_df_map[currentSheet].iterrows(),0,None):
            if index < len(sheet_to_df_map[currentSheet].index)-1:
                timestamps.append((index,row['timestamp'],sheet_to_df_map[currentSheet].iloc[index+1]['timestamp'])) 
        print("Timestamp list done")
        start = 0
        for index, row in islice(coordDf.iterrows(),0,None):
            ### For checking progress
            if index%1000 == 0:
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
        sensorlength = sheet_to_df_map[currentSheet].shape[0]
        for index in range(dflength): ################################## REMEMBER TO CHANGE THISSSSSSSSSS
            ### For checking progress
            if index%1000 == 0:
                print("Current index is %d" %(index))
            minimum = [start,33]
            for index1 in range(start,sensorlength):
                # Retrieving the time difference in ms betwen sensor and video timestamp
                timediff = calcTimeDiff(coordDf.iloc[index]['Current Timestamp'],sheet_to_df_map[currentSheet].iloc[index1]['timestamp'])
                # Checking for values that have timediff within 33 ms
                if timediff > 33:
                    continue
                elif -33 <= timediff <= 33:
                    if abs(timediff)<= minimum[1]:
                        minimum[0]=index1
                        minimum[1]=abs(timediff)
                else:
                    start = index1
                    break
        
            for name in currentColumns:
              coordDf.loc[index, currentSheet+"_"+name] = sheet_to_df_map[currentSheet].iloc[minimum[0]][name]
            
    print("--- %s seconds ---" % (time.time() - start_time))
            
print(coordDf.head())

coordDf.to_csv("C:\\Users\\ngjun\\Desktop\\FINAL COMPILATION\\" + user "_Compiled.csv",index=False)