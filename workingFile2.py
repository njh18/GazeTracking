# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""
import pandas as pd
from datetime import datetime,timedelta
from itertools import islice
import os
import random
from extractPinCodes import extractPinCodes
from moviepy.editor import *
from videoRotation import videoRotation


thelist = [8,9,10,15,29,38,]

pinCodes_original = extractPinCodes("WenJie", "F:\\DATA\\pinCodes")
list2 = ['2296', '8758', '4145', '1925', '6437', '6300', '7338', '9163', '5598', '7328', '3091', '2065', '9699', '8761', '6662', '4981', '1460', '9099']
for i in thelist:
    print(pinCodes_original[i])

print(len(list2))