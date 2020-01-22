#!/usr/bin/env python

import sys

# Get inputs
a = []
s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()
arg = sys.argv[1].split("=")
header = arg[0]
value = arg[1]

# Find matching header
headers = a[0].split(",")
n = 0
while n < len(headers) and headers[n] != header:
   n += 1

# Print nth header
i = 0
while i < len(a):
   curr = a[i].split(",")[n]
   if curr == value:
      print a[i]
   i += 1
