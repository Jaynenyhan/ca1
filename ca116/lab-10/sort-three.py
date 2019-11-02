#!/usr/bin/env python

a = []

n = 3
i = 0
while i < n:
   a.append(input())
   i = i + 1

maximum = 0
i = 0
while i < len(a):
   if maximum < a[i]:
      maximum = i
   i = i + 1

minimum = a[maximum]
i = 0
while i < len(a):
   if minimum > a[i]:
      minimum = i
   i = i + 1

i = 0
while i < len(a):
   if i != maximum and i != minimum:
      middle = i
   i = i + 1

print a[minimum]
print a[middle]
print a[maximum]
