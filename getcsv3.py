#!/usr/bin/env python
"""Print a field specified by row, column numbers from given csv file.

USAGE:
    %prog csv_filename row_number column_number
"""
import csv
import sys
import numpy as np

LATITUDE_COLUMN = 17
LONGITUDE_COLUMN = 16
STATE_COLUMN = 6
TOTAL_ENTRIES = 8144
hitEntries = 0
																																																																																																																																																																																									

def getElement(row_number, column_number):
   with open('farmers-markets2.csv', 'rb') as f:
     rows = list(csv.reader(f))
     return rows[row_number][column_number]


for x in range(0, TOTAL_ENTRIES):
	try:
    		f1 =  float(getElement(x,LATITUDE_COLUMN))
		f2 =  float(getElement(x,LONGITUDE_COLUMN))
		s1 =  str(getElement(x,STATE_COLUMN))
		
		if(f2 < (-0.606131*f2 - f1 - 84.10002)):
			if(s1 == "Montana" or s1 == "Wyoming" or s1 == "Colorado" or s1 == "North Dakota" or s1 == "South Dakota" or  s1 == "Nebraska" or 
			s1 == "Kansas" or s1 == "Oklahoma" or s1 == "Texas" or s1 == "Minnesota" or s1 == "Iowa" or s1 == "Missouri" or s1 == "Arkansas" or s1 == "Louisiana"):
				hitEntries += 1
				print "Index" + str(x) + "," + str(f1) + "," + str(f2) + "," +  s1 + "," + str(hitEntries)
				

	except ValueError:
		print ""


#(getElement(x,16)) #16 longitude X
#(getElement(x,17)) #17 latitude
#if(y + 0.55x = 55.8734 and -0.174x + y = 37.72)
#if(getElement(x,17) + 0.55*getElement(x,16) > 55.8734) #and (-0.174*getElement(x,16) + getElement(x,17)) < 37.72)


