#!/usr/bin/python

import sys

salesSum = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the weekday, val is the sale amount
#
# All the sales for a particular day will be presented,
# then the key will change and we'll be dealing with the next day
#
# Compute sum of sales per weekday. We will use same script for combiner too.

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesSum
        oldKey = thisKey;
        salesSum = 0

    oldKey = thisKey
    salesSum += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesSum

