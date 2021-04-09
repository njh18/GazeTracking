# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""

import os

############################## DONT RUN THIS UNTIL ITS CONFIRMED!!!!

#Get User
user = "Felix"

# Get the folder directory
folder_directory = "D:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL

## JAVIN
faulty_videos = ['Felix_2021_03_25_14_19_26.mp4', 'Felix_2021_03_25_14_19_57.mp4', 'Felix_2021_03_25_14_21_45.mp4', 'Felix_2021_03_25_14_21_57.mp4', 'Felix_2021_03_25_14_23_15.mp4', 'Felix_2021_03_25_14_23_22.mp4', 'Felix_2021_03_25_14_24_10.mp4', 'Felix_2021_03_25_14_30_49.mp4', 'Felix_2021_03_25_14_31_15.mp4', 'Felix_2021_03_25_14_31_24.mp4', 'Felix_2021_03_25_14_32_38.mp4', 'Felix_2021_03_25_14_32_46.mp4', 'Felix_2021_03_25_14_33_01.mp4', 'Felix_2021_03_25_14_33_09.mp4', 'Felix_2021_03_25_14_33_36.mp4', 'Felix_2021_03_25_14_33_44.mp4', 'Felix_2021_03_25_14_34_19.mp4', 'Felix_2021_03_25_14_37_40.mp4']

for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")