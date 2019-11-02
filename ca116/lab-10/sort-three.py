#!/usr/bin/env python

a = []

# Add 3 items to list a
i = 0
while i < 3:
   a.append(input())
   i = i + 1

# Get position of maximum
i = 0
maximum = i
while i < len(a):
   if a[maximum] < a[i]:
      maximum = i
   i = i + 1

# Get position of minimum
i = 0
minimum = i
while i < len(a):
   if a[i] < a[minimum]:
      minimum = i
   i = i + 1

# Get position that is not the minimum or maximum
i = 0
middle = i
while i < len(a):
   if i != maximum and i != minimum:
      middle = i
   i = i + 1

# Print in increasing order
print a[minimum]
print a[middle]
print a[maximum]
