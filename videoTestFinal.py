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

user = 'JiHui'

# Get current Directory
current_directory = os.getcwd()
    
# Get the folder directory
folder_directory = "F:\\DATA\\" + user
        
# Extract Pin Codes
pinCodes = extractPinCodes(user, "F:\\DATA\\pinCodes") #glen com
        
# Change directory to datasets to get data
os.chdir(folder_directory)
        
# Video rotation
faulty_videos = videoRotationMultiple(user, folder_directory)
        
# Change to directory with rotated videos
os.chdir(folder_directory+"\\rotated")
video_names_rotated = os.listdir()
        
# Sort video_names in case if they are not sorted in order
video_names_rotated.sort()
        
        
for index in faulty_videos:
    userList.append(pinCodes[index])    
        
userFaulty[user] = userList
        
# appends pinCodes
for pincode in userList:
    pinCodes.remove(pincode)
    pinCodes.append(pincode)
        
os.chdir("C:\\Users\\ngjun\\Desktop")
#Write into txt
with open(user+"_updated.txt",'w') as filehandle:
    for num in pinCodes:
        filehandle.write("%s\n"%num)
    
print(userFaulty)
print("--- %s seconds ---" % (time.time() - start_time))
