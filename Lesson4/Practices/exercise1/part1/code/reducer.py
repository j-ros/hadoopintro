#!/usr/bin/python

import sys

#Input is records containing (word, nodeID) for each word in the record body sorted by word (tab delimited).
#
#For each word, output a sorted list with the (unique) nodeID where it appears and a count of the times
#it appears in the record body.

oldKey = None
indexes = []
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisIndex = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", sorted(set(indexes)), "\t", count
        oldKey = thisKey;
        indexes = [int(thisIndex)]
		count = 0

    oldKey = thisKey
    indexes.append(int(thisIndex))
    count += 1

if oldKey != None:
    print oldKey, "\t", sorted(set(indexes)), "\t", count

