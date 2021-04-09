# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:46:01 2020

@author: Jun Hso
"""
import os
from videoRotation import videoRotationTest
from extractPinCodes import extractPinCodes
import time
start_time = time.time()
userFaulty={}

#list of users
userList = []

user = 'Eden'

# Get current Directory
current_directory = os.getcwd()
    
# Get the folder directory
folder_directory = "D:\\DATA\\" + user
        
# Extract Pin Codes
try:
    pinCodes = extractPinCodes(user +"_updated", "D:\\DATA\\pinCodes") #glen com
except FileNotFoundError:
    pinCodes = extractPinCodes(user, "D:\\DATA\\pinCodes")
    
print(pinCodes)
        
# Change directory to datasets to get data
os.chdir(folder_directory)
        
# Video rotation
faulty_videos = videoRotationTest(user, folder_directory)
        
# Change to directory with rotated videos
os.chdir(folder_directory)

        
# 
firstCounter = 0
secondCounter = 0
faultyVideoNames = []
for index in faulty_videos:
    if index[0] > 99:
        current = index[0] - 100
        userList.append(pinCodes[faulty_videos[current]])    
        secondCounter += 1
    else:
        current = index[0]
        userList.append(pinCodes[current])
        faultyVideoNames.append(index[1])
        firstCounter += 1

print(userList)
#userFaulty[user] = userList
print(firstCounter)
print(secondCounter)
print(faultyVideoNames)
pinCodesNew = []
# appends pinCodes
for pincode in userList:
    pinCodes.remove(pincode)
    pinCodes.append(pincode)
    pinCodesNew.append(pincode)

#remove all videos
for video in faultyVideoNames:
    os.remove(video)
    
        
os.chdir("C:\\Users\\ngjun\\Desktop\\Pin Codes after Fast Test\\")
#Write into txt
with open(user+"_updated.txt",'w') as filehandle:
    for num in pinCodes:
        filehandle.write("%s\n"%num)
        
with open(user+"_left.txt",'w') as filehandle:
    for num in pinCodesNew:
        filehandle.write("%s\n"%num)
    
print(userFaulty)
print("--- %s seconds ---" % (time.time() - start_time))
