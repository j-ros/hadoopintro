#!/usr/bin/python

import sys
import csv
import re

# Read forum_node.tsv with csv.reader as it contains line breaks in its fields.
#
# It contains 19 fields by record and we are interested in field 0 (nodeID) and field 4 (body)
# Discard first line (nodeID is "id").
#
# Split words in body field and output (word, nodeID) for each word that appears 
# in the body of the records (tab delimited).

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if len(line) != 19 or line[0] == "id":
		continue

	nodeID = line[0].strip()
	body = line[4].strip()

	words = re.split(r'[.,!?:;\"()<>\[\]#$=\-\/\s]', body.lower())

	for word in words:
		print "{0}\t{1}".format(word,nodeID)


