#!/usr/bin/python

# We receive data in the format tagname\t1
#
# Have to compute sum of appearances for each tag and output top 10.
#
# We will use a temp dict to store tag and appearances.

import sys
from heapq import nlargest
from operator import itemgetter

def reducer():
    oldKey = None
    tag_dict = {}
    sumTotal = 0

    for line in sys.stdin:
        data_mapped = line.strip().split('\t')
	if len(data_mapped) == 2:
		thisKey, thisValue = data_mapped
	
		#Check if key changed and process oldKey saved answers
		if oldKey and oldKey != thisKey: 
		    #Add oldKey to dictionary
		    tag_dict[oldKey] = sumTotal
		    #reset temp variables
		    sumTotal = 0

		oldKey = thisKey

		#Process thisKey value
		sumTotal += int(thisValue)
		

    if oldKey != None: #last key
		#Add oldKey to dictionary
		tag_dict[oldKey] = sumTotal
        	#Print top 10
		for tag, value in nlargest(10, tag_dict.iteritems(), key=itemgetter(1)):
			print tag, '\t', value

reducer()
        
