#!/usr/bin/env python
# coding: utf-8

# After creating a single csv file with the data from all volumes(mergedsheets.csv) and parsing the xml files for the volumes (xml_metadata.csv),
# we merge the two files to create a final csv file 'xmljpegmerge.csv' which is used to identify image files from which to remove marginalia.

import csv
import pandas as pd
import os

# read the file with xml data
xml = pd.read_csv(r'C:\Users\rdalwadi\Documents\lawpdfs\xml_metadata.csv', index_col = 'filename')

# read the csv file with jpeg data
jpeg = pd.read_csv(r'C:\Users\rdalwadi\Documents\lawpdfs\mergedsheets.csv', index_col = 'filename')
merge = xml.merge(jpeg, on='filename')

# Save to a csv file
merge.to_csv('xmljpegmerge.csv', encoding = 'utf-8', index = 'False')

