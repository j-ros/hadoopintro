#!/usr/bin/python

import sys

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

