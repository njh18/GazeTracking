# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:31:52 2021

@author: Jun Hso
"""
import os
import cv2
from gaze_tracking import GazeTracking
import matplotlib.pyplot as plt
import time

from moviepy.editor import *


#os.chdir(current_directory+"\\Data\\A")

#Get current Directory
current_directory = os.getcwd()

#Change directory to datasets to get data
os.chdir(current_directory+"\\Data\\Xiang\\Rotated")
video_names=os.listdir()

max_x=0
max_y=0
 

# takes in a video
cap = cv2.VideoCapture("JH_2021_03_01_18_41_12_rotated.mp4")
gaze = GazeTracking()


# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

pupil_coord = []
pupil_coord_head_only=[]
pupil_coord_eye_only=[]
eye_onlys = []
start_time = time.time()

# Read until video is completed
while(cap.isOpened()):
# Capture frame-by-frame
    ret, frame = cap.read()
    now = time.time()

    if ret == True:
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        #Annotating the frame with coordinates
        frame = gaze.annotated_frame()
        text = ""
    
        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"


        #Initialising coordinates
        left_pupil = gaze.pupil_left_coords()
        left_pupil_head_only = gaze.pupil_left_coords_head_only()
        left_pupil_eye_only = gaze.pupil_left_coords_eye_only()
        


        if left_pupil is None:
            print("Cant find pupil")
            pass
        else:
            pupil_coord.append((left_pupil[0], left_pupil[1], now-start_time))
            print(pupil_coord)

        if left_pupil_head_only is None:
            pass
        else:
            pupil_coord_head_only.append((left_pupil_head_only[0], left_pupil_head_only[1], now-start_time))

        if left_pupil_eye_only is None:
            pass
        else:
            pupil_coord_eye_only.append((left_pupil_eye_only[0], left_pupil_eye_only[1], now-start_time))


        cv2.putText(frame, text, (90, 60),
        cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        cv2.putText(frame, text, (90, 60),
        cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130),
                cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165),
                cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "ratio: " + str(gaze.horizontal_ratio()),
                (90, 195), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        cv2.imshow("Demo", frame)


        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    
    # break the loop
    else:
        break 

print(pupil_coord)
print(pupil_coord_head_only)
print(pupil_coord_eye_only)