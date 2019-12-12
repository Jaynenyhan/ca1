#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()

ns = []
s = raw_input()
while s != "end":
   ns.append(s)
   s = raw_input()

t = a[int(ns[0])]
i = 1
while i < len(ns):
   curr = ns[i]
   if curr == "":
      print t
      t = a[int(ns[i + 1])]
      i += 1
   else:
      t = t + " " + a[int(curr)]
   i += 1

print t
