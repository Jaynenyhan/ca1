#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
   ints = int(s)
   a.append(ints)
   s = raw_input()

n = input()
i = 0
while i < len(a):
   print a[i] + n
   i = i + 1
