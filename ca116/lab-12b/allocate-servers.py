#!/usr/bin/env python

# Get inputs
a = []
s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

# Keep count of required servers
count = 1
i = 1
while i < len(a):
   if a[i] < a[i - 1] + 1000:
      count += 1
   i += 1

print count
