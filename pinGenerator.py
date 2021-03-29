# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:42:04 2021

@author: Jun Hso
"""

import random
import pandas as pd
import os

def pinGenerator(num):
    counter = 0
    listofnumbers = []
    
    while counter<num:
        current = ""
        for i in range(4):
            current += str(random.randint(0,9))
        
        listofnumbers.append(current)
        counter+=1
        
    return listofnumbers


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

while True:
    name = input("Name:  ")

    if hasNumbers(name)==True:
        print("This is not a proper name")
    else:
        break



while True:
    num = input("Number of pins required:  ")
    try:
        val = int(num)
        break;
    except ValueError:
        print("This is not an integer. Please enter a valid integer")
        


current_directory = os.getcwd()
os.chdir(current_directory+"\\pinCodes")

value = pinGenerator(val)
print(value)
#Write into txt
with open(name+".txt",'w') as filehandle:
    for num in value:
        filehandle.write("%s\n"%num)
