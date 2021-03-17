# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:37:24 2021

@author: Jun Hso
"""

import os

# get directory
directory = "C:\\Users\\Jun Hso\\Documents\\GitHub\\GazeTracking\\Data\\JHPrac"
os.chdir(directory)


def extractPinCodes(textfile):
    text_file = open(textfile, "r")
    pin_codes = [line[:-1] for line in text_file]
    return
