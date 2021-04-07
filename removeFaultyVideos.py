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
user = "CiEn"

# Get the folder directory
folder_directory = "F:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
if 'rotated' in videos:
    videos.remove('rotated')


# MANUAL FILL

## JAVIN
faulty_videos = ['CiEn_2021_03_31_14_52_34.mp4', 'CiEn_2021_03_31_14_52_42.mp4', 'CiEn_2021_03_31_14_53_20.mp4', 'CiEn_2021_03_31_14_53_27.mp4', 'CiEn_2021_03_31_14_53_33.mp4', 'CiEn_2021_03_31_14_53_39.mp4', 'CiEn_2021_03_31_14_53_45.mp4', 'CiEn_2021_03_31_14_53_51.mp4', 'CiEn_2021_03_31_14_53_58.mp4', 'CiEn_2021_03_31_14_54_04.mp4', 'CiEn_2021_03_31_14_54_10.mp4', 'CiEn_2021_03_31_14_54_16.mp4', 'CiEn_2021_03_31_14_54_24.mp4', 'CiEn_2021_03_31_14_55_07.mp4', 'CiEn_2021_03_31_14_55_13.mp4', 'CiEn_2021_03_31_14_55_25.mp4', 'CiEn_2021_03_31_14_55_47.mp4', 'CiEn_2021_03_31_14_56_09.mp4', 'CiEn_2021_03_31_14_57_19.mp4', 'CiEn_2021_03_31_14_58_22.mp4', 'CiEn_2021_03_31_14_58_40.mp4']
for video in faulty_videos:
    os.remove(video)
 
# ONLY FOR FINAL PROCESSING
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")