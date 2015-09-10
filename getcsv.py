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

"""
for x in range(0, 8144):
	print x
	if (getElement(x,IS_VEGETABLE) == 'Y'):
		if(getElement(x,IS_HONEY) != 'Y' and getElement(x,IS_JAMS) != 'Y'): #or getElement(x,IS_MAPLE) == 'Y'):
			isTrueCount += 1
print isTrueCount
"""


#Problem 2
"""
stateCounts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for x in range(0, 8144):
	if(getElement(x,6) == "Alabama"):
		stateCounts[0] += 1		
	elif(getElement(x,6) == "Alaska"):
		stateCounts[1] += 1
	elif(getElement(x,6) == "Arizona"):
		stateCounts[2] += 1
	elif(getElement(x,6) == "Arkansas"):
		stateCounts[3] += 1
	elif(getElement(x,6) == "California"):
		stateCounts[4] += 1
	elif(getElement(x,6) == "Colorado"):
		stateCounts[5] += 1
	elif(getElement(x,6) == "Connecticut"):
		stateCounts[6] += 1
	elif(getElement(x,6) == "Delaware"):
		stateCounts[7] += 1
	elif(getElement(x,6) == "Florida"):
		stateCounts[8] += 1
	elif(getElement(x,6) == "Georgia"):
		stateCounts[9] += 1
	elif(getElement(x,6) == "Hawaii"):
		stateCounts[10] += 1		
	elif(getElement(x,6) == "Idaho"):
		stateCounts[11] += 1
	elif(getElement(x,6) == "Illinois"):
		stateCounts[12] += 1
	elif(getElement(x,6) == "Indiana"):
		stateCounts[13] += 1
	elif(getElement(x,6) == "Iowa"):
		stateCounts[14] += 1
	elif(getElement(x,6) == "Kansas"):
		stateCounts[15] += 1
	elif(getElement(x,6) == "Kentucky"):
		stateCounts[16] += 1
	elif(getElement(x,6) == "Louisiana"):
		stateCounts[17] += 1
	elif(getElement(x,6) == "Maine"):
		stateCounts[18] += 1
	elif(getElement(x,6) == "Maryland"):
		stateCounts[19] += 1
	elif(getElement(x,6) == "Massachusetts"):
		stateCounts[20] += 1		
	elif(getElement(x,6) == "Michigan"):
		stateCounts[21] += 1
	elif(getElement(x,6) == "Minnesota"):
		stateCounts[22] += 1
	elif(getElement(x,6) == "Mississippi"):
		stateCounts[23] += 1
	elif(getElement(x,6) == "Missouri"):
		stateCounts[24] += 1
	elif(getElement(x,6) == "Montana"):
		stateCounts[25] += 1
	elif(getElement(x,6) == "Nebraska"):
		stateCounts[26] += 1
	elif(getElement(x,6) == "Nevada"):
		stateCounts[27] += 1
	elif(getElement(x,6) == "New Hampshire"):
		stateCounts[28] += 1
	elif(getElement(x,6) == "New Jersey"):
		stateCounts[29] += 1
	elif(getElement(x,6) == "New Mexico"):
		stateCounts[30] += 1		
	elif(getElement(x,6) == "New York"):
		stateCounts[31] += 1
	elif(getElement(x,6) == "North Carolina"):
		stateCounts[32] += 1
	elif(getElement(x,6) == "North Dakota"):
		stateCounts[33] += 1
	elif(getElement(x,6) == "Ohio"):
		stateCounts[34] += 1
	elif(getElement(x,6) == "Oklahoma"):
		stateCounts[35] += 1
	elif(getElement(x,6) == "Oregon"):
		stateCounts[36] += 1
	elif(getElement(x,6) == "Pennsylvania"):
		stateCounts[37] += 1
	elif(getElement(x,6) == "Rhode Island"):
		stateCounts[38] += 1
	elif(getElement(x,6) == "South Carolina"):
		stateCounts[39] += 1
	elif(getElement(x,6) == "South Dakota"):
		stateCounts[40] += 1		
	elif(getElement(x,6) == "Tennessee"):
		stateCounts[41] += 1
	elif(getElement(x,6) == "Texas"):
		stateCounts[42] += 1
	elif(getElement(x,6) == "Utah"):
		stateCounts[43] += 1
	elif(getElement(x,6) == "Vermont"):
		stateCounts[44] += 1
	elif(getElement(x,6) == "Virginia"):
		stateCounts[45] += 1
	elif(getElement(x,6) == "Washington"):
		stateCounts[46] += 1
	elif(getElem
ent(x,6) == "West Virginia"):
		stateCounts[47] += 1
	elif(getElement(x,6) == "Wisconsin"):
		stateCounts[48] += 1
	elif(getElement(x,6) == "Wyoming"):
		stateCounts[49] += 1
	elif(getElement(x,6) == "District of Columbia"):
		stateCounts[50] += 1
	print stateCounts
"""


farmersMarkets = [140, 31, 81, 92, 754, 157, 156, 29, 224, 138, 95, 69, 336, 171, 229, 92, 131, 66, 93, 147, 289, 330, 185, 82, 245, 66, 93, 46, 96, 139, 69, 637, 229, 63, 300, 69, 173, 290, 57, 127, 38, 99, 183, 40, 100, 245, 159, 90, 286, 41, 35]


statePops = [4779736,710231,6392017,2915918,37253956,5029196,3574097,897934,18801310,9687653,1360301,1567582,12830632,6483802,3046355,2853118,4339367,4533372,1328361,5773552,6547629,
9883640,5303925,2967297,5988927,989415,1826341,2700551,1316470,8791894,2059179,19378102,9535483,672591,11536504,3751351,3831074,12702379,1052567,4625364,814180,6346105,25145561,2763885,
625741,8001024,6724540,1852994,5686986,563626,604453]


statePop = {
	'AL':4779736,
	'AK':710231,
	'AZ':6392017,
	'AR':2915918,
	'CA':37253956,
	'CO':5029196,
	'CT':3574097,
	'DE':897934,
	'FL':18801310,
	'GA':9687653,
	'HI':1360301,
	'ID':1567582,
	'IL':12830632,
	'IN':6483802,
	'IA':3046355,
	'KS':2853118,
	'KY':4339367,
	'LA':4533372,
	'ME':1328361,
	'MD':5773552,
	'MA':6547629,
	'MI':9883640,
	'MN':5303925,
	'MS':2967297,
	'MO':5988927,
	'MT':989415,
	'NE':1826341,
	'NV':2700551,
	'NH':1316470,
	'NJ':8791894,
	'NM':2059179,
	'NY':19378102,
	'NC':9535483,
	'ND':672591,
	'OH':11536504,
	'OK':3751351,
	'OR':3831074,
	'PA':12702379,
	'RI':1052567,
	'SC':4625364,
	'SD':814180,
	'TN':6346105,
	'TX':25145561,
	'UT':2763885,
	'VT':625741,
	'VA':8001024,
	'WA':6724540,
	'WV':1852994,
	'WI':5686986,
	'WY':563626,
	'DC':604453
}

maximum = 0
max_index = 0
minimum = 0
minimum_index = 0



for x in range(0, 51):
	print farmersMarkets[x]

for x in range(0, 51):
	print statePops[x]

"""
print type(farmersMarkets[0])
print type(statePops[0])
print type(farmersMarkets[0]/statePops[0])
print farmersMarkets[0]
print statePops[0]

print float(farmersMarkets[0]/statePops[0]) * 1000000000
print float(farmersMarkets[1]/statePops[1])
print float(farmersMarkets[2]/statePops[2])
print float(farmersMarkets[3]/statePops[3])
print float(farmersMarkets[4]/statePops[4])
print float(farmersMarkets[5]/statePops[5])

print statePops[0]/farmersMarkets[0]

for x in range(0, 50):
	statePops[0]/farmersMarkets[0]
	#print farmersMarkets[x]
	#print statePops[x]

"""

"""
for x in range(0, 50):
	if(maximum <  farmersMarkets[x]/statePop.values()[x]):
		maximum = statePop.values()[x]/farmersMarkets[x]
		max_index = x
	if(minimum > statePop.values()[x]/farmersMarkets[x]):
		minimum = statePop.values()[x]/farmersMarkets[x]
		minimum_index = x
	print statePop.values()[x]/farmersMarkets[x]

print "Ok glass take a picture!"
print maximum
print max_index
print "Ok glass take a picture!"
print minimum
print minimum_index

"""
