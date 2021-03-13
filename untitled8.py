# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:30:42 2021

@author: Jun Hso
"""
import pandas as pd


#Reads excel file and converts into df
# can use pd.read_csv instead for csv files
df = pd.read_excel("C:\\Users\\Jun Hso\\Desktop\\Project Part 1 DATA SET WOOOO.xlsx")

print(df.head())



def returnEmployeeDetails(EmpID):
    condition =  df["EmpID"] == EmpID
    
    #filter out the employee's details
    employeeDetails = df[condition]
    
    #filter out the employee name and deptID only
    return employeeDetails[["Employee_Name","DeptID"]]


print (returnEmployeeDetails(10055))
