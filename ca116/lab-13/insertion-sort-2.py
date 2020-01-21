#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()
n = input()

b = []
i = 0
while i < len(a) and a[i] <= n:
   b.append(a[i])
   i += 1

b.append(n)

while i < len(a):
   b.append(a[i])
   i += 1

print b
