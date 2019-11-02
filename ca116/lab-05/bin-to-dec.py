#!/usr/bin/env python

s = raw_input()
t = 0

i = 0
while i < len(s):
   if int(s[i]) == 0:
      t = t * 2
   else:
      t = t * 2 + 1
   i = i + 1

print t
