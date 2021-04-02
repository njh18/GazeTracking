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
user = "JiHui"

# Get the folder directory
folder_directory = "F:\\DATA\\" + user
os.chdir(folder_directory)
videos = os.listdir()
videos.remove('rotated')

# get csv files
coordDf = pd.read_csv("C:\\Users\\ngjun\\Desktop\\compiledCoordinates\\"+ user +"_coordinates_1.csv",
                      dtype = {'Pin Code':str})

pinCodes = coordDf['Pin Code'].unique()

faulty =['8855','2598','7222','7527','2855','5142','9205','2711','2431','5202'
 '4328','7720','1622','1071','7269','8235','0058','2222','5293','2297','1287']

print(coordDf)
print(coordDf[~coordDf['Pin Code'].isin(faulty)])
print(coordDf[coordDf['Pin Code'].isin(faulty)])


# MANUAL FILL
faulty_videos = ['JiHui_2021_03_31_10_06_39.mp4', 'JiHui_2021_03_31_10_07_21.mp4', 'JiHui_2021_03_31_10_07_50.mp4', 'JiHui_2021_03_31_10_08_25.mp4', 'JiHui_2021_03_31_10_08_47.mp4', 'JiHui_2021_03_31_10_09_35.mp4', 'JiHui_2021_03_31_10_09_41.mp4', 'JiHui_2021_03_31_10_10_46.mp4', 'JiHui_2021_03_31_10_11_57.mp4', 'JiHui_2021_03_31_10_13_24.mp4', 'JiHui_2021_03_31_10_13_52.mp4', 'JiHui_2021_03_31_10_14_52.mp4', 'JiHui_2021_03_31_10_15_08.mp4', 'JiHui_2021_03_31_10_15_56.mp4', 'JiHui_2021_03_31_10_17_50.mp4', 'JiHui_2021_03_31_10_18_38.mp4', 'JiHui_2021_03_31_10_19_29.mp4', 'JiHui_2021_03_31_10_19_35.mp4', 'JiHui_2021_03_31_10_19_51.mp4', 'JiHui_2021_03_31_10_19_57.mp4', 'JiHui_2021_03_31_10_20_09.mp4']
pincodes = ['8855' '2598' '7222' '7527' '2855' '5142' '9205' '2711' '2431' '5202'
 '4328' '7720' '1622' '1071' '7269' '8235' '0058' '2222' '5293' '2297'
 '1287']


for video in faulty_videos:
    os.remove(video)
    
os.chdir(folder_directory + "\\rotated")
for video in faulty_videos:
    os.remove(video[:-4]+"_rotated"+".mp4")