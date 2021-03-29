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

os.chdir("F:\\DATA\\")
print(os.listdir())

['ShengRong', 'JingYi', 'YanRu', 'Winnchis', 'Xavier', 'ZhiYu', 'FungRu', 'Clarence', 'Kelvin', 'PekKoon', 'WeiSheng']