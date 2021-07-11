# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""

import os

############################## DONT RUN THIS UNTIL ITS CONFIRMED!!!!

#Get User
user = "Aaron"

# Get the folder directory
folder_directory = "E:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL
faulty_videos = ['Aaron_2021_05_06_16_10_33.mp4', 'Aaron_2021_05_06_16_11_00.mp4', 'Aaron_2021_05_06_16_12_49.mp4', 'Aaron_2021_05_06_16_12_56.mp4', 'Aaron_2021_05_06_16_13_47.mp4', 'Aaron_2021_05_06_16_14_06.mp4', 'Aaron_2021_05_06_16_14_21.mp4', 'Aaron_2021_05_06_16_14_27.mp4', 'Aaron_2021_05_06_16_15_02.mp4', 'Aaron_2021_05_06_16_15_11.mp4', 'Aaron_2021_05_06_16_15_18.mp4', 'Aaron_2021_05_06_16_15_30.mp4', 'Aaron_2021_05_06_16_15_37.mp4', 'Aaron_2021_05_06_16_15_43.mp4', 'Aaron_2021_05_06_16_15_51.mp4', 'Aaron_2021_05_06_16_16_05.mp4', 'Aaron_2021_05_06_16_16_11.mp4', 'Aaron_2021_05_06_16_16_17.mp4', 'Aaron_2021_05_06_16_16_53.mp4', 'Aaron_2021_05_06_16_17_07.mp4', 'Aaron_2021_05_06_16_17_13.mp4', 'Aaron_2021_05_06_16_18_02.mp4', 'Aaron_2021_05_06_16_18_56.mp4', 'Aaron_2021_05_06_16_19_02.mp4', 'Aaron_2021_05_06_16_19_08.mp4', 'Aaron_2021_05_06_16_19_15.mp4', 'Aaron_2021_05_06_16_19_21.mp4', 'Aaron_2021_05_06_16_19_34.mp4', 'Aaron_2021_05_06_16_19_53.mp4', 'Aaron_2021_05_06_16_19_59.mp4', 'Aaron_2021_05_06_16_20_05.mp4', 'Aaron_2021_05_06_16_20_52.mp4', 'Aaron_2021_05_06_16_21_38.mp4', 'Aaron_2021_05_06_16_22_46.mp4', 'Aaron_2021_05_06_16_22_52.mp4', 'Aaron_2021_05_06_16_22_58.mp4', 'Aaron_2021_05_06_16_23_04.mp4', 'Aaron_2021_05_06_16_23_13.mp4', 'Aaron_2021_05_06_16_23_19.mp4', 'Aaron_2021_05_06_16_23_25.mp4', 'Aaron_2021_05_06_16_23_47.mp4', 'Aaron_2021_05_06_16_23_54.mp4', 'Aaron_2021_05_06_16_24_00.mp4', 'Aaron_2021_05_06_16_24_06.mp4', 'Aaron_2021_05_06_16_24_13.mp4', 'Aaron_2021_05_06_16_24_21.mp4']


for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")