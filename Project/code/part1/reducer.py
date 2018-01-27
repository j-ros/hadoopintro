#!/usr/bin/python

# We receive data in the format author_id\thour
#
# Have to compute hour that appears in most registers for each author_id (if tie print all in different lines)
# in the format author_id\thour
#
# We will use a temp list to store how many times each hour appears for each author_id then print the max when author_id 
# changes. Hours go from 00 to 23.

import sys

def reducer():
    oldKey = None
    hours = [0] * 24

    for line in sys.stdin:
        data_mapped = line.strip().split('\t')
	if len(data_mapped) == 2:
		thisKey, thisHour = data_mapped
	
		#Check if key changed and process oldKey saved hours
		if oldKey and oldKey != thisKey: 
		    #Find max
		    maxHour = 0
		    for hour in hours:
			if hour > maxHour:
				maxHour = hour
		    #Now print all lines with hour = maxHour
		    for i, hour in enumerate(hours): 
			if hour == maxHour:
				print oldKey, '\t', i
		    #reset temp variables
		    hours = [0] * 24

		oldKey = thisKey

		#Process thisKey hours
		hours[int(thisHour)] += 1
		

    if oldKey != None: #last key
        	#Find max
		maxHour = 0
		for hour in hours:
		    if hour > maxHour:
			maxHour = hour
		#Now print all lines with hour = maxHour
		for i, hour in enumerate(hours): 
			if hour == maxHour:
				print oldKey, '\t', i

reducer()
        
