# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:46:01 2020

@author: Jun Hso
"""
import os
from videoRotation import videoRotationMultiple
from extractPinCodes import extractPinCodes
import time
start_time = time.time()
userFaulty={}

#list of users
userList = []

user = "Eden"

# Get current Directory
current_directory = os.getcwd()
    
# Get the folder directory
folder_directory = "D:\\DATA\\" + user
        
        
# Change directory to datasets to get data
os.chdir(folder_directory)
        
# Video rotation
faulty_videos = videoRotationMultiple(user, folder_directory)
        
# Change to directory with rotated videos
os.chdir(folder_directory+"\\rotated")
      

# Extract Pin Codes
try:
    pinCodes = extractPinCodes(user +"_updated", "C:\\Users\\ngjun\\Desktop\\Pin Codes after Fast Test\\") #glen com
except FileNotFoundError:
    pinCodes = extractPinCodes(user, "C:\\Users\\ngjun\\Desktop\\Pin Codes after Fast Test\\")
    
print(pinCodes)    

# 
firstCounter = 0
secondCounter = 0

for index in faulty_videos:
    if index> 99:
        current = index - 100
        userList.append(pinCodes[faulty_videos[current]])    
        secondCounter += 1
    else:
        current = index
        userList.append(pinCodes[current])
        firstCounter += 1

print(userList)
print(firstCounter)
print(secondCounter)


# appends pinCodes
for pincode in userList:
    pinCodes.remove(pincode)
    pinCodes.append(pincode)
        
os.chdir("C:\\Users\\ngjun\\Desktop\\")
#Write into txt
with open(user+"_updated.txt",'w') as filehandle:
    for num in pinCodes:
        filehandle.write("%s\n"%num)
    
print(userFaulty)
print("--- %s seconds ---" % (time.time() - start_time))
