#!/usr/bin/env python

# Get inputs
a = []
s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()
n = input()

# Print
i = 0
while i < len(a):
   print a[i].split(",")[n]
   i += 1
