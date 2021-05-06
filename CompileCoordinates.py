# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:30:41 2021     

@author: ngjun
"""
import pandas as pd

#Get User
user = "Gwendolyn"

# get csv files
coordDf = pd.read_csv("C:\\Users\\ngjun\\Desktop\\compiledCoordinates\\"+ user +"_coordinates.csv",
                      dtype = {'Pin Code':str})

coordDf2 = pd.read_csv("C:\\Users\\ngjun\\Desktop\\compiledCoordinates\\"+ user +"_coordinates_1.csv",
                      dtype = {'Pin Code':str})

faulty = coordDf2['Pin Code'].unique()


coordDf = coordDf[~coordDf['Pin Code'].isin(faulty)]

combined = pd.concat([coordDf,coordDf2])
combined = combined.reset_index()
combined = combined.drop(columns=['index'])


combined.to_csv("C:\\Users\\ngjun\\Desktop\\compiledCoordinates\\"+ user +"_coordinates_final.csv",index=False)