#!/usr/bin/env python

s = raw_input()
t = ""

i = 0
while i < len(s):
   if s[i] == " ":
      i = i + 1
   else:
      t = t + s[i]
      i = i + 1

print t
