# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

# Import everything needed to edit video clips
from moviepy.editor import *
import os


def videoRotation(video_name, current_directory):
    # Creates a new folder for resizing
    rotated_folder = current_directory + "\\rotated"
    if not os.path.exists(rotated_folder):
        os.makedirs(rotated_folder)

    # loading video
    clip1 = VideoFileClip(video_name)

    # rename video_name
    new_video_name = video_name[:-4]+"_rotated"+".mp4"

    if clip1.fps >240:
        print(video_name + " is faulty")
    else:
        # changing the rotation of video
        if clip1.rotation in (90, 270):
            clip1 = clip1.resize(clip1.size[::-1])
            clip1.rotation = 0
    
        # moving to folder to save video
        os.chdir(rotated_folder)
    
        # saving the video
        clip1.write_videofile(new_video_name)
    return


def videoRotationMultiple(user, current_directory):

    # Make sure it is in correct directory
    if os.getcwd() != current_directory:
        os.chdir(current_directory)

    # Get list of names in the directory
    list_of_video_names = os.listdir()
    list_of_video_names.sort()
    
    # Remove Sensorsfolder in list of video names
    sensorsFile = user + "_Sensors"

    if sensorsFile in list_of_video_names:
        list_of_video_names.remove(sensorsFile)

    ###############REMOVE THIS NEXT TIME################
    print(list_of_video_names)
    print(len(list_of_video_names))

    # Creates a new folder for resizing
    rotated_folder = current_directory + "\\rotated"
    video_names_rotated = []

    if os.path.exists(rotated_folder):
        os.chdir(rotated_folder)
        list_of_video_names.remove("rotated")
        video_names_rotated = os.listdir()
        # all videos are rotated
        if len(video_names_rotated) == len(list_of_video_names):
            return
    else:
        os.makedirs(rotated_folder)
    
    counter = 0
    faulty_videos = []
    for video_name in list_of_video_names:
        print("-------" + "Processing " +
              str(counter+1) + " out of " + str(len(list_of_video_names)) + " videos now" + "-------")
        # Making sure its in the right directory
        if os.getcwd() != current_directory:
            os.chdir(current_directory)

        # loading video
        clip1 = VideoFileClip(video_name)

        # rename video_name
        new_video_name = video_name[:-4]+"_rotated"+".mp4"
        
        if clip1.fps >120:
            print(video_name + " is faulty")
            print(counter)
            faulty_videos.append(counter)
        else:
            if new_video_name not in video_names_rotated:
                # changing the rotation of video
                if clip1.rotation in (90, 270):
                    clip1 = clip1.resize(clip1.size[::-1])
                    clip1.rotation = 0
    
                # moving to folder to save video
                os.chdir(rotated_folder)
    
                # saving the video
                clip1.write_videofile(new_video_name, audio = False, threads = 4)
    
                print("------------------" + video_name +
                      " rotated!" + "------------------")
            else:
                print("Video already rotated!")

        counter += 1
        clip1.close()
        
    return faulty_videos


def videoRotationTest(user,current_directory):
        # Make sure it is in correct directory
    if os.getcwd() != current_directory:
        os.chdir(current_directory)

    # Get list of names in the directory
    list_of_video_names = os.listdir()
    list_of_video_names.sort()
    
    # Remove Sensorsfolder in list of video names
    sensorsFile = user + "_Sensors"

    if sensorsFile in list_of_video_names:
        list_of_video_names.remove(sensorsFile)

    ###############REMOVE THIS NEXT TIME################
    print(list_of_video_names)
    print(len(list_of_video_names))

    # Creates a new folder for resizing
    rotated_folder = current_directory + "\\rotated"

    if os.path.exists(rotated_folder):
        list_of_video_names.remove("rotated")
    
    counter = 0
    faulty_videos = []
    for video_name in list_of_video_names:
        print("-------" + "Processing " +
              str(counter+1) + " out of " + str(len(list_of_video_names)) + " videos now" + "-------")
        # Making sure its in the right directory
        if os.getcwd() != current_directory:
            os.chdir(current_directory)

        # loading video
        clip1 = VideoFileClip(video_name)

        # rename video_name
        new_video_name = video_name[:-4]+"_rotated"+".mp4"
        
        if clip1.fps >120:
            print(video_name + " is faulty")
            print(counter)
            faulty_videos.append((counter,video_name))

        counter += 1
        clip1.close()
        
    return faulty_videos