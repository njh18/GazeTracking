# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

import os

# get directory
directory = "C:\\Users\\Jun Hso\\Documents\\GitHub\\GazeTracking\\Data\\JHprac"
os.chdir(directory)
video_names = os.listdir()
print(video_names)

user = "JHprac"
sensorsFile = user + "_Sensors"

if sensorsFile in video_names:
    video_names.remove(sensorsFile)
    print("filename removed")

print(video_names)
