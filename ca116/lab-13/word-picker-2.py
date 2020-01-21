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

# Ok so no output if no numbers, so build string if numbers exist
if ns[0]:
   t = a[int(ns[0])] + " "
i = 1
while i < len(ns):
   curr = ns[i]
   if ns[i] == "":
      t = t + "\n"
   else:
      t = t + a[int(curr)] + " "
   i += 1

print t
