#!/usr/bin/env python

n = input()
m = input()
print m

i = 0
while i < n - 1:
   if m % 2 == 0:
      m = m / 2
   else:
      m = (m * 3) + 1
   print m
   i = i + 1
