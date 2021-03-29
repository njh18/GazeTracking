# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:46:01 2020

@author: Jun Hso
"""
import os
from videoRotation import videoRotationMultiple
from extractPinCodes import extractPinCodes

listOfUsers = ['Felix', 'JingYi', 'YanRu', 'Winnchis', 'ZhiYu', 'FungRu', 'Clarence', 'Kelvin', 'PekKoon', 'WeiSheng', 'Alphaeus']

userFaulty={}

for user in listOfUsers:
    #list of users
    userList = []
    
    # Get current Directory
    current_directory = os.getcwd()
    
    # Get the folder directory
    folder_directory = "E:\\DATA\\" + user
        
    # Extract Pin Codes
    pinCodes = extractPinCodes(user, "E:\\DATA\\pinCodes") #glen com
        
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
        
    for pincode in userList:
        pinCodes.remove(pincode)
        
    os.chdir("C:\\Users\\ngjun\\OneDrive\\Desktop")
    #Write into txt
    with open(user+"_updated.txt",'w') as filehandle:
        for num in pinCodes:
            filehandle.write("%s\n"%num)
    
    print(userFaulty)