#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()

smallest = 0
i = 0
while i < len(a):
   if a[i] < a[smallest]:
      smallest = i
   i = i + 1

print smallest
