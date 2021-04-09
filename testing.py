# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:14:11 2021

@author: Jun Hso
"""

import os
import pandas as pd
import shutil


first = "Beverley-2021-03-02_18-26-40"
second = "Beverley2-2021-03-02_19-00-20"

path2 = "C:\\Users\\Jun Hso\\Desktop\\" + second + "\\"
os.chdir(path2)
filename2 = os.listdir()
print(filename2)

path1 = "C:\\Users\\Jun Hso\\Desktop\\" + first + "\\"
os.chdir(path1)
filename1 = os.listdir()
print(filename1)


path3 = "C:\\Users\\Jun Hso\\Desktop\\"+ first + "\\" + first + "\\"
if os.path.exists(path3) == False:
    os.makedirs(path3)


for file in filename2:
    try:
        df1 = pd.read_csv(path1 + file)
        print(df1.shape)
    except:
        df1 = pd.DataFrame({'A' : []})
    
    os.chdir(path2)
    try:    
        df2 = pd.read_csv(path2 + file)
        print(df2.shape)
    except:
        df2 = pd.DataFrame({'A' : []})
        
    if df1.empty and df2.empty:
        shutil.copy(path1 + file, path3 + file)
    elif df1.empty :
        df3 = df2
        print(df3.shape)
        os.chdir(path3)
        df3.to_csv(path3 + file)
    elif df2.empty:
        df3 = df1
        print(df3.shape)
        os.chdir(path3)
        df3.to_csv(path3 + file)
    else:
        df3 =  pd.concat([df1,df2])
        print(df3.shape)
        
        os.chdir(path3)
        df3.to_csv(path3 + file)