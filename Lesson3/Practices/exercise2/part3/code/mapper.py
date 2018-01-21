#!/usr/bin/python

# Format of each line is:
# ip\sid\susername\sdatetime\szone\smethod\spath\request\sstatus\ssize
#
# We want elements path, striping common  part so as to group same paths together 
# We need to write them out to standard output

import sys

strip = 'http://www.the-associates.co.uk'
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, username, datetime, zone, method, path, request, status, size = data
	if(strip in path): 
		path = path.replace(strip,"")
        print "{0}".format(path)

