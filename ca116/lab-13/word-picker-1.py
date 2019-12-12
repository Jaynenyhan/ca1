#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()

ns = []
s = raw_input()
while s != "end":
   integer = int(s)
   ns.append(integer)
   s = raw_input()

i = 0
while i < len(ns):
   curr = ns[i]
   print a[curr]
   i += 1
