# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:55:51 2021

@author: Jun Hso
"""

# Import everything needed to edit video clips 
from moviepy.editor import *
import os

#Get current Directory
current_directory = os.getcwd()

#Moves into directory with data
os.chdir(current_directory+"\\Data\\Xiang\\rotated")
current_directory = os.getcwd()

#Get a list of names in the directory
list_of_video_names=os.listdir()
print(list_of_video_names)

for video_name in list_of_video_names:
    new_name= "Xiang" + video_name[2:-4] + ".mp4"
    os.rename(video_name,new_name)