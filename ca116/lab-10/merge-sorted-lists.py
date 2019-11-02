#!/usr/bin/env python

a = []
b = []
sl = []

# Get inputs
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()
s = raw_input()
while s != "end":
   integer = int(s)
   b.append(integer)
   s = raw_input()

# Compare last items of each list
# Add largest to new list and remove it from original list
while a != [] and b != []:
   if a[len(a) - 1] > b[len(b) - 1]:
      sl.append(a[len(a) - 1])
      a.pop()
   else:
      sl.append(b[len(b) - 1])
      b.pop()

# Add remaining items to new list without comparing
# Avoid index out of range error
if a != []:
   sl.append(a[len(a) - 1])
   a.pop()
elif b != []:
   sl.append(b[len(b) - 1])
   b.pop()

# Print new list backwards, therefore smallest -> largest
i = 0
while i < len(sl):
   print sl[len(sl) - i - 1]
   i = i + 1
