#!/usr/bin/python

# We need to write each line from the forum_node.tsv file and extract 
# for nodes with node_type equals question (field 6) the tagnames (field 3) (there could be more than 1, 
# get all in different lines)
#
# Return tagname\t1

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
	if line[0] == "id" or len(line) != 19: #skip headers and wrong lines
		continue
	else:
		if line[5] == 'question':
			tagnames = line[2].split(' ')
			for tag in tagnames:
				print tag, '\t', 1
		else:
			continue

mapper()

