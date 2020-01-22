#!/usr/bin/env python

import sys

# Get inputs
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
if ns != []:
   t = a[int(ns[0])]
# Continue building string
# Problem: spaces between words, newline if empty input
# Case 1: empty -> newline
# Case 2: word, prev is empty -> dont add space
# Case 3: word, prev is word -> add space
i = 1
while i < len(ns):
   currword = ns[i]
   prevword = ns[i - 1]
   if currword == "":
      t = t + "\n"
   elif prevword == "":
      t = t + a[int(currword)]
   else:
      t = t + " " + a[int(currword)]
   i += 1

if i == len(ns):
   sys.stdout.write(t)
