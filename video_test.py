# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:31:52 2021

@author: Jun Hso
"""
import os
import cv2
import pandas as pd
from gaze_tracking import GazeTracking
import matplotlib.pyplot as plt
import time

from moviepy.editor import *
from videoRotation import videoRotation
from extractNames import extractNames

# Change directory to datasets to get data
os.chdir("C:\\Users\\Jun Hso\\Desktop")
current_directory = os.getcwd()


######################Change this when necessary #################################
video_name = "JHprac_2021_03_12_13_11_26.mp4"
new_video_name = video_name[:-4]+"_rotated"+".mp4"

#Getting Videoinformation
video_info = extractNames(video_name)
print(video_info)

# rotating the video
video_rotation(video_name, current_directory)

# takes in a video
os.chdir(current_directory+"\\rotated")

cap = cv2.VideoCapture(new_video_name)
gaze = GazeTracking()


# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

pupil_coord = []
pupil_coord_head_only = []
pupil_coord_eye_only = []
eye_onlys = []
start_time = time.time()


# Create new dataframe for output
column_names = ["Timeframe","X-Coord (Both)","Y-Coord (Both)","X-Coord (Head)","Y-Coord (Head)","X-Coord (Eye)","Y-Coord (Eye)"]
new_df = pd.DataFrame(columns = column_names)
print(new_df)


# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    now = time.time()
    if ret == True:
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        # Annotating the frame with coordinates
        frame = gaze.annotated_frame()
        text = ""

        milliseconds = cap.get(cv2.CAP_PROP_POS_MSEC)

        seconds = milliseconds//1000
        milliseconds = (milliseconds%1000)/1000
        timeframe = seconds + milliseconds
        
        #forcombining with datetime
        #tdelta = pd.to_timedelta(df["Miliseconds"], unit="ms")
        
        
        if seconds >= 60:
            minutes = seconds//60
            seconds = seconds % 60

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        # Initialising coordinates
        left_pupil = gaze.pupil_left_coords()
        left_pupil_head_only = gaze.pupil_left_coords_head_only()
        left_pupil_eye_only = gaze.pupil_left_coords_eye_only()

        if left_pupil is None:
            both_x = 0
            both_y = 0
        else:
            both_x = left_pupil[0]
            both_y = left_pupil[1]

        if left_pupil_head_only is None:
            head_x = 0
            head_y = 0
            pass
        else:
            head_x = left_pupil_head_only[0]
            head_y = left_pupil_head_only[1]

        if left_pupil_eye_only is None:
            eye_x = 0
            eye_y = 0
        else:
            eye_x = left_pupil_eye_only[0]
            eye_y = left_pupil_eye_only[1]

  
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)


        cv2.imshow("Demo", frame)


        #Input all the calcuated values into new dataframe
        new_row = {"Timeframe":timeframe,"X-Coord (Both)":both_x,"Y-Coord (Both)":both_y,
                   "X-Coord (Head)":head_x,"Y-Coord (Head)":head_y,"X-Coord (Eye)":eye_x,"Y-Coord (Eye)":eye_y}
        new_df = new_df.append(new_row,ignore_index=True)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # break the loop
    else:
        break


print(new_df)
