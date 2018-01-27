#!/usr/bin/python

# We need to write each line from the forum_node.tsv file and extract 
# - if node type (field 6) is question then grab id (field 1) and length of body (field 4)
# - if node type (field 6) is answer then grab parent_id (field 7) and length of body (field 4)
# and add tags to distinguish question from answer in reducer ('Q', 'A').
#
# Return id\t'Q'\tlength(body) for questions
# and parent_id\t'A'\tlength(body) for answers

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    for line in reader:
	if line[0] == "id" or len(line) != 19: #skip headers and wrong lines
		continue
	else:
		if line[5] == 'question':
			result = [line[0], 'Q', len(line[4])]
		elif line[5] == 'answer':
			result = [line[6], 'A', len(line[4])]
		else:
			continue
		
		writer.writerow(result)

mapper()

