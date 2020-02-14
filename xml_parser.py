#!/usr/bin/env python
# coding: utf-8

import xml.etree.ElementTree as ET
import csv
import pandas as pd
import os
import urllib

# Using the search.csv file, a list of the volumes whose xml files will be parsed is created. 
with open("search.csv","r") as xmlfiles:
    reader=csv.DictReader(xmlfiles)
    l=[d['xmlfiles'] for d in reader] # The column xmlfiles contains the identifiers of the volumes

# Through the xml files, extract the logical page numbers(pageNum), physical page numbers(leafNum) 
# and leaf hand side(handSide)
handSide = []
pageNum = []
filename = []
leafNum = []
master = []

for i in l:
    try:
        # Get the xml file of a volume by creating a download link using volume identifier
        xml = urllib.request.urlopen('https://archive.org/download/' + i + '/' + i + '_' + 'scandata.xml') 
        tree = ET.parse(xml)
        root = tree.getroot()

        # Create a master list with xml metadata for all volumes
        for page in root[2].findall('page'):
            leafNum.append(int(page.attrib['leafNum']))
            handSide.append(page.find('handSide').text)

            page_dict = {}
            page_dict['leafNum'] = int(page.attrib['leafNum'])
            if page.find('pageNumber') != None:
                page_dict['pageNum'] = page.find('pageNumber').text
            else:
                page_dict['pageNum'] = ''

            page_dict['handSide'] = page.find('handSide').text
            page_dict['filename'] = i + '_' + '%04d' %  page_dict['leafNum']
            master.append(page_dict)

        # Create a csv file
        with open('xml_metadata.csv', 'w') as csvfile:
            writer1 = csv.DictWriter(csvfile, fieldnames=['filename','leafNum','handSide','pageNum'],lineterminator='\n')
            writer1.writeheader()
            for row in master:
                writer1.writerow(row)
    except:
        print(i)

