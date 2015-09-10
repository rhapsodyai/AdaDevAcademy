#!/usr/bin/env python
"""Print a field specified by row, column numbers from given csv file.

USAGE:
    %prog csv_filename row_number column_number
"""
import csv
import sys
import numpy as np

HERB_COLUMN = 30
STATE_COLUMN = 6
TOTAL_ENTRIES = 8144
TOTAL_COLUMNS = 45
hitEntries = 0
times = 0
																																																																																																																																																																																							

def getElement(row_number, column_number):
   with open('farmers-markets2.csv', 'rb') as f:
     rows = list(csv.reader(f))
     return rows[row_number][column_number]


for x in range(0, TOTAL_ENTRIES):
	try:
		#print str(times) + "," + getElement(0,x)
		#times += 1

		if(getElement(x,HERB_COLUMN) == "Y" and getElement(x,STATE_COLUMN) == "New York" or getElement(x,STATE_COLUMN) == "California" ):
			print "HIT AT " + str(x)
			hitEntries +=1
		times +=1

	except ValueError:
		print ""

print "Total percentage of herbs monopolized by New York and California is " + str(float(hitEntries)/float(times))

""" Column and Index
0,FMID
1,MarketName
2,Website
3,street
4,city
5,County
6,State
7,zip
8,Season1Date
9,Season1Time
10,Season2Date
11,Season2Time
12,Season3Date
13,Season3Time
14,Season4Date
15,Season4Time
16,Longitude
17,Latitude
18,Location
19,Credit
20,WIC
21,WICcash
22,SFMNP
23,SNAP
24,Bakedgoods
25,Cheese
26,Crafts
27,Flowers
28,Eggs
29,Seafood
30,Herbs
31,Vegetables
32,Honey
33,Jams
34,Maple
35,Meat
36,Nursery
37,Nuts
38,Plants
39,Poultry
40,Prepared
41,Soap
42,Trees
43,Wine
44,updateTime
"""
