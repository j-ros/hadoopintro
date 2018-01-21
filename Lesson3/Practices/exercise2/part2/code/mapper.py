#!/usr/bin/python

# Format of each line is:
# ip\sid\susername\sdatetime\szone\smethod\spath\request\sstatus\ssize
#
# We want elements ip 
# We need to write them out to standard output

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, username, datetime, zone, method, path, request, status, size = data
        print "{0}".format(ip)

