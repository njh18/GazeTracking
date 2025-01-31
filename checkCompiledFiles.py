# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

import pandas as pd
import os
from extractPinCodes import extractPinCodes


#Get User
user = "Aaron"
# get csv files
coordDf = pd.read_csv("C:\\Users\\Jun Hso\\Desktop\\Compiled Coordinates\\"+ user +"_coordinates.csv",
                      dtype = {'Pin Code':str})
pinCodes = coordDf['Pin Code'].unique()


print(len(pinCodes))

######################################################## Finding out the number of errors #################################################
errors = []
for i in range(len(pinCodes)):
    # No 1
  sampleDf = coordDf[coordDf['Pin Code'] == pinCodes[i]]
  sampleDfZero = sampleDf[sampleDf['Left X-Coord (Both)'] == 0]
  error = round(sampleDfZero.shape[0]*100/sampleDf.shape[0],2)
  if error > 10:
    errors.append((pinCodes[i],i,error))


#### no 2
print(errors)
print(len(errors))









####### OUTPUT THE DATA into a txt file to re-record

# Extract Pin Codes, Either the updated one or the non updated one
try:
    pinCodes_original  = extractPinCodes(user +"_updated", "C:\\Users\\Jun Hso\\Desktop\\") #glen com
except FileNotFoundError:
    pinCodes_original  = extractPinCodes(user, "C:\\Users\\Jun Hso\\Desktop\\")
    
# Put all the pincodes with error in a list
pinCodesNew = []
for value in errors:
    pinCodesNew.append(value[0])
    
# Remove pinCode Errors from list
for pincode in pinCodesNew:
    pinCodes_original.remove(pincode)

# Get the folder directory
folder_directory = "E:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')

videos.sort()

faulty_videos = []
for value in errors:
    faulty_videos.append(videos[value[1]])

print(faulty_videos)
######################### WRITING INTO TEXT FILES #####################################
os.chdir("C:\\Users\\Jun Hso\\Desktop\\Final Pin Code Updates\\")
with open(user+"_error.txt",'w') as filehandle:
    for num in pinCodesNew:
        filehandle.write("%s\n"%num)    
    
with open(user+"_remaining.txt",'w') as filehandle:
    for num in pinCodes_original:
        filehandle.write("%s\n"%num)        

for pincode in pinCodesNew:
    pinCodes_original.append(pincode)
    
with open(user+"_updated.txt",'w') as filehandle:
    for num in pinCodes_original:
        filehandle.write("%s\n"%num)     