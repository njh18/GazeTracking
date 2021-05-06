# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:46:01 2020

@author: Jun Hso
"""
import os
import cv2
from gaze_tracking import GazeTracking
import time
import pandas as pd
import datetime
from extractNames import extractNames, formatTime
from extractPinCodes import extractPinCodes
start_time = time.time()
#list of users

userList = ["Nico"]

for user in userList:
    # Get current Directory
    current_directory = os.getcwd()
    
    folder_directory = "D:\\DATA\\" + user
    #folder_directory = "F:\\DATA\\" + user #glen com
    
    
    # Extract Pin Codes
    try:
        pinCodes = extractPinCodes(user +"_updated", "C:\\Users\\ngjun\\Desktop\\") #glen com
    except FileNotFoundError:
        pinCodes = extractPinCodes(user, "C:\\Users\\ngjun\\Desktop\\")
    
    print(pinCodes)

    
    # Change to directory with rotated videos
    os.chdir(folder_directory+"\\rotated")
    video_names_rotated = os.listdir()
    
    # Sort video_names in case if they are not sorted in order
    video_names_rotated.sort()
    print(video_names_rotated)  # CHECKPOINT
    
    # Create new dataframe for output
    column_names = ["Pin Code", "Video Timestamp", "Time Passed", 
                    "Left X-Coord (Both)", "Left Y-Coord (Both)", "Right X-Coord (Both)", "Right Y-Coord (Both)", 
                    "Left X-Coord (Head)", "Left Y-Coord (Head)", "Right X-Coord (Head)", "Right Y-Coord (Head)",
                    "Left X-Coord (Eye)", "Left Y-Coord (Eye)", "Right X-Coord (Eye)", "Right Y-Coord (Eye)"]
    new_df = pd.DataFrame(columns=column_names)
    
    for num in range(len(video_names_rotated)):
            # Just to check progress of loop
        print("processing " + str(num+1) + " out of " +
              str(len(video_names_rotated)) + " videos")
        
        print("Current pin code is : %s" % (pinCodes[num]))
        
        # Extracting timestamp from video_names_rotated
        names = extractNames(video_names_rotated[num])
        video_timestamp = names['Timestamp']
        
        #### inputs needed
        #### video_name
        #### new_df
        
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
        
                # Initialising coordinates
                left_pupil = gaze.pupil_left_coords()
                left_pupil_head_only = gaze.pupil_left_coords_head_only()
                left_pupil_eye_only = gaze.pupil_left_coords_eye_only()
                right_pupil = gaze.pupil_right_coords()
                right_pupil_head_only = gaze.pupil_right_coords_head_only()
                right_pupil_eye_only = gaze.pupil_right_coords_eye_only()
        
                if gaze.pupils_located is True:
                    #both movements
                    both_x_left = left_pupil[0]
                    both_y_left = left_pupil[1]
                    both_x_right = right_pupil[0]
                    both_y_right = right_pupil[1]
                    #Head Movements only
                    head_x_left = left_pupil_head_only[0]
                    head_y_left = left_pupil_head_only[1]
                    head_x_right = right_pupil_head_only[0]
                    head_y_right = right_pupil_head_only[1]
                    #Eye Movements only
                    eye_x_left = left_pupil_eye_only[0]
                    eye_y_left = left_pupil_eye_only[1]
                    eye_x_right = right_pupil_eye_only[0]
                    eye_y_right = right_pupil_eye_only[1]
                else:
                    both_x_left = 0
                    both_y_left = 0
                    both_x_right = 0
                    both_y_right = 0
                    head_x_left = 0
                    head_y_left = 0
                    head_x_right = 0
                    head_y_right = 0
                    eye_x_left = 0
                    eye_y_left = 0
                    eye_x_right = 0
                    eye_y_right = 0
        
                # Input all the calcuated values into new dataframe
                new_row = {"Pin Code": pinCodes[num], "Video Timestamp": video_timestamp, "Time Passed": milliseconds,
                               "Left X-Coord (Both)": both_x_left, "Left Y-Coord (Both)": both_y_left,
                               "Right X-Coord (Both)": both_x_right, "Right Y-Coord (Both)": both_y_right, 
                               "Left X-Coord (Head)": head_x_left, "Left Y-Coord (Head)": head_y_left, 
                               "Right X-Coord (Head)": head_x_right , "Right Y-Coord (Head)": head_y_right, 
                               "Left X-Coord (Eye)": eye_x_left, "Left Y-Coord (Eye)": eye_y_left,
                               "Right X-Coord (Eye)": eye_x_right, "Right Y-Coord (Eye)": eye_y_right}
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
    
    print(new_df.head(10))
    
    # Cleaning Datafram
    tdelta = pd.to_timedelta(new_df["Time Passed"], unit="ms")
    new_df["Current Timestamp"] = new_df["Video Timestamp"] + tdelta
    new_df["Current Timestamp"] = new_df["Current Timestamp"].apply(formatTime)
    print(new_df['Current Timestamp'])
    
    #pathName = "C:\\Users\\ngjun\\OneDrive\\Desktop\\compiledCoordinates\\" #glen com
    pathName = "C:\\Users\\ngjun\\desktop\\compiledCoordinates\\"
    if os.path.exists(pathName + user + "_coordinates" + ".csv"):
        new_df.to_csv(pathName + user + "_coordinates_1" + ".csv",index=False)
    else:
        new_df.to_csv(pathName + user + "_coordinates" + ".csv",index=False)

print("--- %s seconds ---" % (time.time() - start_time))