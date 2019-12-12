#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()
n = input()

i = 0
while i < len(a) and a[i] <= n:
   i += 1

print i
