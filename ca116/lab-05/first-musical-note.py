#!/usr/bin/env python

t = ""
s = raw_input()

i = 0
while i < len(s):
   if "a" <= s[len(s) - i - 1] and s[len(s) - i - 1] <= "g":
      t = s[len(s) - i - 1]
   i = i + 1

print t
