#!/usr/bin/env python

a = []
less = []
greater = []

# Get inputs
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()
n = input()

# Separate items from list 'a' into new lists 'less' and 'greater'
i = 0
while i < len(a):
   if a[i] <= n:
      less.append(a[i])
   elif a[i] > n:
      greater.append(a[i])
   i = i + 1

# Print each item is list 'less', then 'n', then each item in list 'greater'
i = 0
while i < len(less):
   print less[i]
   i = i + 1

print n

i = 0
while i < len(greater):
   print greater[i]
   i = i + 1
