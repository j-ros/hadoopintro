#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	if len(line) != 19 or line[0] == "id":
		continue

	nodeID = line[0].strip()
	body = line[4].strip()

	words = re.split(r'[.,!?:;\"()<>\[\]#$=\-\/\s]', body.lower())

	for word in words:
		print "{0}\t{1}".format(word,nodeID)


