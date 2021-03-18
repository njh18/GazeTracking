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
from videoRotation import videoRotationMultiple

# Get current Directory
current_directory = os.getcwd()
folder_directory = "C:\\Users\\Jun Hso\\Desktop\\Xiang"

# Change directory to datasets to get data
os.chdir(folder_directory)

# Video rotation
video_rotation_multiple(folder_directory)

# Change to directory with rotated videos
os.chdir(folder_directory+"\\rotated")
video_names_rotated = os.listdir()

print(video_names_rotated)  # CHECKPOINT###

# This is to help with scaling of x and y axis
# initialise variables
max_x = 0
max_y = 0


for num in range(len(video_names_rotated)):

    # Just to check progress of loop
    print("processing " + str(num+1) + " out of " +
          str(len(video_names_rotated)) + " videos")

    # takes in a video
    cap = cv2.VideoCapture(video_names_rotated[num])
    gaze = GazeTracking()

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    pupil_coord = []
    pupil_coord_head_only = []
    pupil_coord_eye_only = []
    start_time = time.time()

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

            # Initialising coordinates
            left_pupil = gaze.pupil_left_coords()
            left_pupil_head_only = gaze.pupil_left_coords_head_only()
            left_pupil_eye_only = gaze.pupil_left_coords_eye_only()

            if left_pupil is None:
                pass
            else:
                pupil_coord.append(
                    (left_pupil[0], left_pupil[1], now-start_time))

            if left_pupil_head_only is None:
                pass
            else:
                pupil_coord_head_only.append(
                    (left_pupil_head_only[0], left_pupil_head_only[1], now-start_time))

            if left_pupil_eye_only is None:
                pass
            else:
                pupil_coord_eye_only.append(
                    (left_pupil_eye_only[0], left_pupil_eye_only[1], now-start_time))

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

    # initialise lists
    x_coord = []
    y_coord = []
    timing = []

    x_coord_head_only = []
    y_coord_head_only = []
    timing_head_only = []

    x_coord_eye_only = []
    y_coord_eye_only = []
    timing_eye_only = []

    ############## For head movements ##############

    # first x-coord & y-coord
    normalx = pupil_coord[0][0]
    normaly = pupil_coord[0][1]

    for i in range(len(pupil_coord)):
        x_coord.append(normalx-pupil_coord[i][0])
        y_coord.append(normaly-pupil_coord[i][1])
        timing.append(pupil_coord[i][2])

    ############## For head only movements ##############

    # first x-coord & y-coord
    normalx_head_only = pupil_coord_head_only[0][0]
    normaly_head_only = pupil_coord_head_only[0][1]

    for i in range(len(pupil_coord_head_only)):
        x_coord_head_only.append(normalx_head_only-pupil_coord_head_only[i][0])
        y_coord_head_only.append(normaly_head_only-pupil_coord_head_only[i][1])
        timing_head_only.append(pupil_coord_head_only[i][2])

   ############## For eye only ##############

   # first x-coord & y-coord
    normalx_eye_only = pupil_coord_eye_only[0][0]
    normaly_eye_only = pupil_coord_eye_only[0][1]

    for i in range(len(pupil_coord_eye_only)):
        x_coord_eye_only.append(normalx_eye_only-pupil_coord_eye_only[i][0])
        y_coord_eye_only.append(normaly_eye_only-pupil_coord_eye_only[i][1])
        timing_eye_only.append(pupil_coord_eye_only[i][2])

    # Plot
    fig = plt.figure(1)
    fig.suptitle("With Both Head and Pupil Movements")
    plt.subplot(4, 3, num+1)
    plt.scatter(x_coord,  y_coord, c=timing, cmap='winter', zorder=3)
    plt.title(video_names_rotated[num])
    plt.grid(b=True, color='#BEBEBE', zorder=0)
    plt.xlim(-60, 60)
    plt.ylim(-150, 150)
    plt.subplots_adjust(wspace=1, hspace=1)

    # Plots
    fig2 = plt.figure(2)
    fig2.suptitle("Head Movements only")
    plt.subplot(4, 3, num+1)
    plt.scatter(x_coord_head_only, y_coord_head_only,
                c=timing_head_only, cmap='winter', zorder=3)
    plt.title(video_names_rotated[num])
    plt.grid(b=True, color='#BEBEBE', zorder=0)
    plt.xlim(-60, 60)
    plt.ylim(-150, 150)
    plt.subplots_adjust(wspace=1, hspace=1)

    # Plots
    fig3 = plt.figure(3)
    fig3.suptitle("Eye Movements only")
    plt.subplot(4, 3, num+1)
    plt.scatter(x_coord_eye_only, y_coord_eye_only,
                c=timing_eye_only, cmap='winter', zorder=3)
    plt.title(video_names_rotated[num])
    plt.grid(b=True, color='#BEBEBE', zorder=0)
    plt.xlim(-60, 60)
    plt.ylim(-150, 150)
    plt.subplots_adjust(wspace=1, hspace=1)

    # To find out whats the max coordinates
    max_x_coords = [max(x_coord), max(x_coord_eye_only),
                    max(x_coord_head_only)]
    max_y_coords = [abs(min(y_coord)), abs(
        min(y_coord_eye_only)), abs(min(y_coord_eye_only))]

    if max(max_x_coords) > max_x:
        max_x = max(max_x_coords)
    if max(max_y_coords) > max_y:
        max_y = max(max_y_coords)
