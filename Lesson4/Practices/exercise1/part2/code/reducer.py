#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data
#
# We will read all lines corresponding to same id, but user line not always be first. We will save user line 
# and an array of forum lines and when we change id we combine all forum lines with user line and write.

import sys

def reducer():
    oldKey = None
    userLine = None
    forumLines = []

    for line in sys.stdin:
        data_mapped = line.strip().split('\t')

		thisKey = data_mapped[0]
		
		#Check if key changed and process oldKey saved lines
		if oldKey and oldKey != thisKey: 
			for post in forumLines: #merge and print all forum lines
				print('\t'.join(map(str,post + userLine[1:])))
			#reset temp variables
			userLine = None 
			forumLines = []

		oldKey = thisKey

		#Same key. Process line.
		if data_mapped[1] == '"A"':
			data_mapped.pop(1) #remove 'A' tag
			userLine = data_mapped #and save in userLine temp variable
		elif data_mapped[1] == '"B"':
			data_mapped.pop(1) #remove 'B' tag
			forumLines.append(data_mapped) #and add to forumLines temp list
		else:
			# Something has gone wrong. Skip this line.
			continue

    if oldKey != None: #last key
        for post in forumLines:
	    print('\t'.join(map(str,post + userLine[1:])))

reducer()
        
