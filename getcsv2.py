#!/usr/bin/env python
"""Print a field specified by row, column numbers from given csv file.

USAGE:
    %prog csv_filename row_number column_number
"""
import csv
import sys

#3843

#With maple
#3869
#3569 -1 adjusted

NUMBER_OF_ROWS = 8144

IS_BAKEDGOODS = 24
ARE_WINES = 43

IS_VEGETABLE = 31
IS_HONEY = 32
IS_JAMS = 33
IS_MAPLE = 34
isTrueCount = 0

#row_number = int(sys.argv[1])
#column_number = int(sys.argv[2])



def getElement(row_number, column_number):
   with open('farmers-markets2.csv', 'rb') as f:
     rows = list(csv.reader(f))
     return rows[row_number][column_number]

#Problem #1
#if 32 && 33 >> 34 >> 35
for x in range(0, 8144):
	if (getElement(x,IS_VEGETABLE) == 'Y'):
		if(getElement(x,IS_HONEY) == 'Y' or getElement(x,IS_JAMS) == 'Y'): #and getElement(x,IS_MAPLE) != 'Y' and getElement(x,IS_BAKEDGOODS) != 'Y' and getElement(x,ARE_WINES) != 'Y'): #or getElement(x,IS_MAPLE) == 'Y'):
			isTrueCount += 1
print isTrueCount
