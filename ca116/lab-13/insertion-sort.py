#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()

i = 1
while i < len(a):
   v = a[i]
   p = i
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p -= 1
   a[p] = v
   i += 1

i = 0
while i < len(a):
   print a[i]
   i += 1
