# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:12:45 2021

@author: Jun Hso
"""

# Import everything needed to edit video clips 
from moviepy.editor import *
import os
from video_rotation import *

#Get current Directory
current_directory = os.getcwd()

#Moves into directory with data
os.chdir(current_directory+"\\Data\\Xiang")
current_directory = os.getcwd()

#Run video rotation
video_rotation_multiple(current_directory)

