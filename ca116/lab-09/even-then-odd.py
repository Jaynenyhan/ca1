#!/usr/bin/env python

even = []
odd = []

s = raw_input()
while s != "end":
   integer = int(s)
   if integer % 2 == 0:
      even.append(integer)
   else:
      odd.append(integer)
   s = raw_input()

# Print evens one by one
i = 0
while i < len(even):
   print even[i]
   i = i + 1

# Print odds one by one
i = 0
while i < len(odd):
   print odd[i]
   i = i + 1
