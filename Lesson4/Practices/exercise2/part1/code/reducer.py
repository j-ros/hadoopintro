#!/usr/bin/python

import sys

salesSum = 0
salesRecord = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the weekday, val is the sale amount
#
# All the sales for a particular day will be presented,
# then the key will change and we'll be dealing with the next day
#
# Compute average sales per weekday

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesSum/salesRecord
        oldKey = thisKey;
        salesSum = 0
	salesRecord = 0

    oldKey = thisKey
    salesSum += float(thisSale)
    salesRecord += 1

if oldKey != None:
    print oldKey, "\t", salesSum/salesRecord

