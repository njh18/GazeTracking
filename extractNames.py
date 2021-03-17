# -*- coding: utf-8 -*-
from datetime import datetime as dt
import datetime as datetime

def formatTime(t):
    if t.microsecond % 1000 >= 500:  # check if there will be rounding up
        t = t + datetime.timedelta(milliseconds=1)  # manually round up
    return t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def extractNames(video_name):
    '''
    Parameters
    ----------
    video_name : STRING
        name of video

    Returns
    -------
    name : DICTIONARY
        'User' : Name of user that recorded video
        'Timestamp': Timestamp of the recorded video
    '''
    # Create Dictionary
    names = {}

    # finding the first underscore to extract the user
    first_underscore = video_name.find("_")
    rotation = video_name.find("rotated")

    # Extracting timestamp and converting to datetime object
    timestamp = video_name[first_underscore+1:rotation-1]
    date_object = dt.strptime(timestamp, "%Y_%m_%d_%H_%M_%S")

    # Save values into dictionary
    names['User'] = video_name[0:first_underscore]
    names['Timestamp'] = date_object

    return names
