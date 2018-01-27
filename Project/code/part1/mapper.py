#!/usr/bin/python

# We need to write each line from the forum_node.tsv file and extract author_id (field 4)
# and parse the hour from the added_at (field 9).
#
# Return author_id\thour

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    for line in reader:
	if line[0] == "id" or len(line) != 19: #skip headers and wrong lines
		continue
	else:
		authorid = int(line[3])
		hour = int(line[8][11:13])
		
		writer.writerow([authorid, hour])

        

mapper()

