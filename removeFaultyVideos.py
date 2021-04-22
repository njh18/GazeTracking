# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""

import os

############################## DONT RUN THIS UNTIL ITS CONFIRMED!!!!

#Get User
user = "MingHao"

# Get the folder directory
folder_directory = "D:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL

## JAVIN
faulty_videos = ['John_2021_04_21_21_15_02.mp4', 'John_2021_04_21_21_15_49.mp4', 'John_2021_04_21_21_18_45.mp4', 'John_2021_04_21_21_20_31.mp4', 'John_2021_04_21_21_21_07.mp4', 'John_2021_04_21_21_25_01.mp4', 'John_2021_04_21_21_26_42.mp4', 'John_2021_04_21_21_26_49.mp4', 'John_2021_04_21_21_26_57.mp4', 'John_2021_04_21_21_27_28.mp4', 'John_2021_04_21_21_28_48.mp4']

for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")