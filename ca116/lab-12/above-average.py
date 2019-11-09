#!/usr/bin/env python

# Get inputs
a = []
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()

# Get average
i = 0
total = 0
while i < len(a):
   total = total + a[i]
   i = i + 1
if len(a) != 0:  # Prevent ZeroDivision error if list empty
   average = float(total) / len(a)

# Print number if above average
i = 0
while i < len(a):
   if average < a[i]:
      print a[i]
   i = i + 1
