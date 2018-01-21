#!/usr/bin/python

import sys

totalHits = 0
oldKey = None
maxKey = None
maxHits = 0

# Loop around the data
# It will be in the format key
# Where key is the path
#
# All the path will be presented,
# then the key will change and we'll be dealing with the next path

for line in sys.stdin:
    data_mapped = line.strip()

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
	if totalHits > maxHits:
		maxKey = oldKey
		maxHits = totalHits
        oldKey = thisKey;
        totalHits = 0

    oldKey = thisKey
    totalHits += 1

if oldKey != None:
	if totalHits > maxHits:
		maxKey = oldKey
		maxHits = totalHits

print "{0}\t{1}".format(maxKey, maxHits)

