# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""
import pandas as pd
from datetime import datetime,timedelta
from itertools import islice
import os
import random
from extractPinCodes import extractPinCodes
from moviepy.editor import *
from videoRotation import videoRotation
import numpy as np

############################## DONT RUN THIS UNTIL ITS CONFIRMED!!!!

#Get User
user = "Xavier"

# Get the folder directory
folder_directory = "F:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL

## JAVIN
faulty_videos = ['Xavier_2021_04_01_16_02_13.mp4', 'Xavier_2021_04_01_16_03_02.mp4', 'Xavier_2021_04_01_16_03_43.mp4', 'Xavier_2021_04_01_16_04_19.mp4', 'Xavier_2021_04_01_16_04_42.mp4', 'Xavier_2021_04_01_16_04_49.mp4', 'Xavier_2021_04_01_16_04_58.mp4', 'Xavier_2021_04_01_16_05_06.mp4', 'Xavier_2021_04_01_16_05_19.mp4', 'Xavier_2021_04_01_16_05_27.mp4', 'Xavier_2021_04_01_16_05_34.mp4', 'Xavier_2021_04_01_16_06_11.mp4', 'Xavier_2021_04_01_16_06_29.mp4', 'Xavier_2021_04_01_16_06_47.mp4', 'Xavier_2021_04_01_16_07_00.mp4', 'Xavier_2021_04_01_16_07_06.mp4', 'Xavier_2021_04_01_16_07_13.mp4', 'Xavier_2021_04_01_16_07_21.mp4', 'Xavier_2021_04_01_16_07_37.mp4', 'Xavier_2021_04_01_16_08_19.mp4', 'Xavier_2021_04_01_16_08_31.mp4', 'Xavier_2021_04_01_16_09_31.mp4', 'Xavier_2021_04_01_16_10_16.mp4', 'Xavier_2021_04_01_16_10_26.mp4', 'Xavier_2021_04_01_16_10_52.mp4', 'Xavier_2021_04_01_16_11_28.mp4', 'Xavier_2021_04_01_16_11_43.mp4', 'Xavier_2021_04_01_16_12_23.mp4', 'Xavier_2021_04_01_16_12_42.mp4', 'Xavier_2021_04_01_16_12_51.mp4', 'Xavier_2021_04_01_16_13_04.mp4']

for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")