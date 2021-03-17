# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:46:01 2020

@author: Jun Hso
"""
import os
import cv2
from gaze_tracking import GazeTracking
import matplotlib.pyplot as plt
import time
import pandas as pd

from videoRotation import videoRotationMultiple
from extractNames import extractNames
from extractPinCodes import extractPinCodes

# Current user
user = "JHprac"

# Get current Directory
current_directory = os.getcwd()
folder_directory = "C:\\Users\\Jun Hso\\Desktop" + "\\" + user

# Change directory to datasets to get data
os.chdir(folder_directory)

# Video rotation
videoRotationMultiple(user, folder_directory)

# Extract Pin Codes
pinCodes = extractPinCodes(user, folder_directory)
print(pinCodes)

# Change to directory with rotated videos
os.chdir(folder_directory+"\\rotated")
video_names_rotated = os.listdir()

# Sort video_names in case if they are not sorted in order
video_names_rotated.sort()

print(video_names_rotated)  # CHECKPOINT

# Create new dataframe for output
column_names = ["Pin Code", "Timeframe", "X-Coord (Both)", "Y-Coord (Both)",
                "X-Coord (Head)", "Y-Coord (Head)", "X-Coord (Eye)", "Y-Coord (Eye)"]
new_df = pd.DataFrame(columns=column_names)
print(new_df)

for num in range(len(video_names_rotated)):

    # Just to check progress of loop
    print("processing " + str(num+1) + " out of " +
          str(len(video_names_rotated)) + " videos")

    print("Current pin code is : %s" % (pinCodes[num]))

    # takes in a video
    cap = cv2.VideoCapture(video_names_rotated[num])
    gaze = GazeTracking()

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

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

            # Getting the timestamp of the frame in milliseconds
            milliseconds = cap.get(cv2.CAP_PROP_POS_MSEC)
            seconds = milliseconds//1000
            milliseconds = (milliseconds % 1000)/1000
            timeframe = seconds + milliseconds

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

            # Input all the calcuated values into new dataframe
            new_row = {"Pin Code": pinCodes[num], "Timeframe": timeframe, "X-Coord (Both)": both_x, "Y-Coord (Both)": both_y,
                       "X-Coord (Head)": head_x, "Y-Coord (Head)": head_y, "X-Coord (Eye)": eye_x, "Y-Coord (Eye)": eye_y}
            new_df = new_df.append(new_row, ignore_index=True)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

    print(new_df)

print(new_df)