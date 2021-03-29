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

os.chdir("E:\\DATA\\Felix")
felix = os.listdir()
felix.sort()
print(felix)
print(felix.index("Felix_2021_03_25_14_36_26.mp4"))

#['ShengRong', 'JingYi', 'YanRu', 'Winnchis', 'Xavier', 'ZhiYu', 'FungRu', 'Clarence', 'Kelvin', 'PekKoon', 'WeiSheng']

os.chdir("C:\\Users\\ngjun\\OneDrive\\Desktop\\videoTest")

video_name = "Xavier_2021_03_26_00_11_03.mp4"

clip1 = VideoFileClip(video_name)

print("Duration: " + str(clip1.duration))
print(clip1.fps)


video_name_faulty = Felix_2021_03_25_14_36_26.mp4

clip2 = VideoFileClip(video_name_faulty)

print("Duration: " + str(clip2.duration))
print(clip2.fps)



