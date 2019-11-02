#!/usr/bin/env python

s = raw_input()
t = ""

i = 0
while i < len(s):
   if i == len(s) - 1:
      t = t + ("*" * int(s[i]))
   else:
      t = t + ("*" * int(s[i])) + "\n"
   i = i + 1

print t
