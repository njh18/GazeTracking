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
from extractPinCodes import extractPinCodes

def format_time(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        # manually round up
        t = t + datetime.timedelta(milliseconds=1)
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def calcTimeDiff(dateobject1,dateobject2):
  timeDiff = dateobject1-dateobject2
  timeDiffMs = timeDiff.total_seconds()*1000
  return timeDiffMs

#Get User
user = "CiEn"

# get csv files
coordDf = pd.read_csv("C:\\Users\\ngjun\\Desktop\\compiledCoordinates\\"+ user +"_coordinates.csv")
pinCodes = coordDf['Pin Code'].unique()

####### Finding out the number of errors
errors = []
for i in range(len(pinCodes)):
  sampleDf = coordDf[coordDf['Pin Code'] == pinCodes[i]]
  sampleDfZero = sampleDf[sampleDf['Left X-Coord (Both)'] == 0]
  error = round(sampleDfZero.shape[0]*100/sampleDf.shape[0],2)
  if error >= 10:
    errors.append((pinCodes[i],i,error))

print(errors)
print(len(errors))

####### OUTPUT THE DATA into a txt file to re-record

# Extract Pin Codes, Either the updated one or the non updated one
try:
    pinCodes_original  = extractPinCodes(user +"_updated", "F:\\DATA\\pinCodes") #glen com
except FileNotFoundError:
    pinCodes_original  = extractPinCodes(user, "F:\\DATA\\pinCodes")
    
# Put all the pincodes with erorr in a list
pinCodesNew = []
for value in errors:
    pinCodesNew.append(pinCodes_original[value[1]])
    
# Remove pinCode Errors from list
for pincode in pinCodesNew:
    pinCodes_original.remove(pincode)


######################### WRITING INTO TEXT FILES #####################################
os.chdir("C:\\Users\\ngjun\\Desktop\\Final Pin Code Updates\\")
with open(user+"_left.txt",'w') as filehandle:
    for num in pinCodesNew:
        filehandle.write("%s\n"%num)    
    
with open(user+"_updated.txt",'w') as filehandle:
    for num in pinCodes_original:
        filehandle.write("%s\n"%num)        
        