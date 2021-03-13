# -*- coding: utf-8 -*-
from datetime import datetime

def extractNames (video_name):
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
    #Create Dictionary
    names = {}
    
    #finding the first underscore to extract the user
    first_underscore = video_name.find("_")
    
    
    #Extracting timestamp and converting to datetime object
    timestamp = video_name[first_underscore+1:-4]
    date_object = datetime.strptime(timestamp,"%Y_%m_%d_%H_%M_%S")

    #Save values into dictionary
    names['User'] = video_name[0:first_underscore]
    names['Timestamp'] = date_object
    
    return names


