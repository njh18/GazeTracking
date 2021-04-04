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
user = "Leonel"

# Get the folder directory
folder_directory = "F:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL

## JAVIN
faulty_videos = ['Leonel_2021_03_30_21_19_34.mp4', 'Leonel_2021_03_30_21_19_53.mp4', 'Leonel_2021_03_30_21_20_02.mp4', 'Leonel_2021_03_30_21_20_11.mp4', 'Leonel_2021_03_30_21_20_23.mp4', 'Leonel_2021_03_30_21_20_31.mp4', 'Leonel_2021_03_30_21_20_39.mp4', 'Leonel_2021_03_30_21_20_47.mp4', 'Leonel_2021_03_30_21_20_54.mp4', 'Leonel_2021_03_30_21_21_02.mp4', 'Leonel_2021_03_30_21_21_09.mp4', 'Leonel_2021_03_30_21_21_16.mp4', 'Leonel_2021_03_30_21_21_38.mp4', 'Leonel_2021_03_30_21_21_46.mp4', 'Leonel_2021_03_30_21_21_54.mp4', 'Leonel_2021_03_30_21_22_03.mp4', 'Leonel_2021_03_30_21_22_10.mp4', 'Leonel_2021_03_30_21_22_18.mp4', 'Leonel_2021_03_30_21_22_26.mp4', 'Leonel_2021_03_30_21_22_40.mp4', 'Leonel_2021_03_30_21_22_48.mp4', 'Leonel_2021_03_30_21_22_54.mp4', 'Leonel_2021_03_30_21_23_01.mp4', 'Leonel_2021_03_30_21_23_07.mp4', 'Leonel_2021_03_30_21_23_13.mp4', 'Leonel_2021_03_30_21_23_19.mp4', 'Leonel_2021_03_30_21_23_37.mp4', 'Leonel_2021_03_30_21_23_45.mp4', 'Leonel_2021_03_30_21_23_52.mp4', 'Leonel_2021_03_30_21_24_01.mp4', 'Leonel_2021_03_30_21_24_07.mp4', 'Leonel_2021_03_30_21_24_12.mp4', 'Leonel_2021_03_30_21_24_18.mp4', 'Leonel_2021_03_30_21_24_24.mp4', 'Leonel_2021_03_30_21_24_29.mp4', 'Leonel_2021_03_30_21_24_35.mp4', 'Leonel_2021_03_30_21_26_06.mp4', 'Leonel_2021_03_30_21_26_12.mp4', 'Leonel_2021_03_30_21_26_19.mp4', 'Leonel_2021_03_30_21_26_32.mp4', 'Leonel_2021_03_30_21_26_42.mp4', 'Leonel_2021_03_30_21_26_54.mp4', 'Leonel_2021_03_30_21_27_00.mp4', 'Leonel_2021_03_30_21_27_05.mp4', 'Leonel_2021_03_30_21_27_12.mp4', 'Leonel_2021_03_30_21_27_33.mp4', 'Leonel_2021_03_30_21_27_58.mp4', 'Leonel_2021_03_30_21_28_15.mp4', 'Leonel_2021_03_30_21_28_26.mp4', 'Leonel_2021_03_30_21_28_32.mp4', 'Leonel_2021_03_30_21_28_43.mp4', 'Leonel_2021_03_30_21_28_49.mp4', 'Leonel_2021_03_30_21_29_00.mp4', 'Leonel_2021_03_30_21_29_08.mp4', 'Leonel_2021_03_30_21_29_13.mp4', 'Leonel_2021_03_30_21_29_19.mp4', 'Leonel_2021_03_30_21_29_25.mp4', 'Leonel_2021_03_30_21_29_31.mp4', 'Leonel_2021_03_30_21_29_37.mp4', 'Leonel_2021_03_30_21_29_45.mp4', 'Leonel_2021_03_30_21_29_51.mp4', 'Leonel_2021_03_30_21_30_20.mp4', 'Leonel_2021_03_30_21_30_26.mp4', 'Leonel_2021_03_30_21_30_32.mp4', 'Leonel_2021_03_30_21_30_44.mp4', 'Leonel_2021_03_30_21_30_50.mp4', 'Leonel_2021_03_30_21_30_55.mp4', 'Leonel_2021_03_30_21_31_43.mp4', 'Leonel_2021_03_30_21_31_49.mp4', 'Leonel_2021_03_30_21_31_59.mp4', 'Leonel_2021_03_30_21_32_06.mp4']

for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")