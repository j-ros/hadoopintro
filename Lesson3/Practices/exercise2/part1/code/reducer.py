#!/usr/bin/python

import sys

totalHits = 0
oldKey = None

# Loop around the data
# It will be in the format key
# Where key is the path
#
# All the paths will be presented,
# then the key will change and we'll be dealing with the next path
#
# Compute totalHits by path

for line in sys.stdin:
    data_mapped = line.strip()

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalHits
        oldKey = thisKey;
        totalHits = 0

    oldKey = thisKey
    totalHits += 1

if oldKey != None:
    print oldKey, "\t", totalHits

