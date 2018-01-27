#!/usr/bin/python

# We need to write each line from the forum_node.tsv file and extract 
# for nodes with node_type equals question (field 6) the author_id (field 4) and id (field 1)
# and for nodes with node_type equals question or comment (field 6) the author_id (field 4) and parent_id (field 7)
#
# Return id/parent_id\tauthor_id

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
	if line[0] == "id" or len(line) != 19: #skip headers and wrong lines
		continue
	else:
		if line[5] == 'question':
			print line[0], '\t', line[3]
		elif line[5] == 'answer' or line[5] == 'comment':
			print line[6], '\t', line[3]
		else:
			continue

mapper()

