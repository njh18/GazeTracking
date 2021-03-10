# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

# Import everything needed to edit video clips 
from moviepy.editor import *
import os

def video_rotation(video_name,current_directory):
    #Creates a new folder for resizing
    rotated_folder = current_directory + "\\rotated"
    if not os.path.exists(rotated_folder):
        os.makedirs(rotated_folder) 

    # loading video
    clip1 = VideoFileClip(video_name)
    
    #rename video_name
    new_video_name = video_name[:-4]+"_rotated"+".mp4"

    # changing the rotation of video
    if clip1.rotation in (90, 270):
        clip1 = clip1.resize(clip1.size[::-1])
        clip1.rotation = 0

    #moving to folder to save video
    os.chdir(rotated_folder)
    
    # saving the video
    clip1.write_videofile(new_video_name)
    return