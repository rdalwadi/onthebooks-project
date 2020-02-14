#!/usr/bin/env python
# coding: utf-8

# The following code merges all the sheets in the excel files and creates a single csv file with data from all the files. 
# Each file consists volume wise data such as the page image filename, logical page number, title of the section
# section type, a link to the jpeg image. The csv concatenates all the data into a single sheet. 

import os
import os.path
from os import path
import csv
import pandas as pd
from pandas import Series
import sys

excel_sheets = ['SectionsRenamed-Privt-Laws-Reso-FileListsForOCR.xlsx','SectionsRenamed-publiclawsFileListOCR.xlsx','SectionsRenamed-PublicLocalSp.xlsx','SectionsRenamedsessionlaws.xlsx'] # Files with the sheets to merge
sheet_to_df_map = []
df_list = []

# For every file read data from all sheets into a dataframe
for file in excel_sheets:
    sheet_to_df_map.append(pd.read_excel(file, sheet_name=None))
    
# Combine the datframes of each sheet into one dataframe for each file
for n in sheet_to_df_map:
    df_list.append(pd.concat(n[frame] for frame in n.keys()))

df1 = df_list[0]
df2 = df_list[1]
df3 = df_list[2]
df4 = df_list[3]

# Concatenate all the dataframes into a single dataframe and save it as a csv file
verticalstack = pd.concat([df1,df2,df3,df4], axis=0)
verticalstack.to_csv('mergedsheets.csv', index =False)


