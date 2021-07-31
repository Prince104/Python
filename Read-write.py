# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:27:11 2021

@author: Prince
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('E:/AEclass/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('E:/AEclass/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('E:/AEclass/User_Data.xlsx')

#df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)