# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""

import os

############################## DONT RUN THIS UNTIL ITS CONFIRMED!!!!

#Get User
user = "Gwendolyn"

# Get the folder directory
folder_directory = "D:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL

## JAVIN
faulty_videos=['Gwendolyn_2021_04_11_11_34_10.mp4', 'Gwendolyn_2021_04_11_11_34_58.mp4', 'Gwendolyn_2021_04_11_11_36_41.mp4', 'Gwendolyn_2021_04_11_11_36_47.mp4', 'Gwendolyn_2021_04_11_11_49_20.mp4', 'Gwendolyn_2021_04_11_12_06_41.mp4', 'Gwendolyn_2021_04_11_13_58_35.mp4', 'Gwendolyn_2021_04_11_13_58_45.mp4', 'Gwendolyn_2021_04_11_13_58_54.mp4', 'Gwendolyn_2021_04_11_13_59_02.mp4', 'Gwendolyn_2021_04_11_13_59_09.mp4', 'Gwendolyn_2021_04_11_13_59_16.mp4', 'Gwendolyn_2021_04_11_14_00_23.mp4', 'Gwendolyn_2021_04_11_14_00_30.mp4', 'Gwendolyn_2021_04_11_14_00_37.mp4', 'Gwendolyn_2021_04_11_14_00_44.mp4', 'Gwendolyn_2021_04_11_14_00_51.mp4', 'Gwendolyn_2021_04_11_14_01_01.mp4', 'Gwendolyn_2021_04_11_14_07_16.mp4', 'Gwendolyn_2021_04_11_14_07_24.mp4']
for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")