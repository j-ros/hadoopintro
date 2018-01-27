#!/usr/bin/python

# We receive data in the format id/parent_id\tauthor_id
#
# Have to list all author_id for a specific id/parent_id (if there are author_id repeated list them multiple times)

import sys

def reducer():
    oldKey = None
    author_list = []

    for line in sys.stdin:
        data_mapped = line.strip().split('\t')
	if len(data_mapped) == 2:
		thisKey, thisValue = data_mapped
	
		#Check if key changed and process oldKey saved answers
		if oldKey and oldKey != thisKey: 
		    print oldKey, '\t', author_list
		    author_list = []

		oldKey = thisKey

		#Process thisKey value
		author_list.append(int(thisValue))
		

    if oldKey != None: #last key
		print oldKey, '\t', author_list

reducer()
        
