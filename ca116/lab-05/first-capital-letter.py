#!/usr/bin/env python

position = 0
s = raw_input()

i = 0
while i < len(s):
   if "A" <= s[len(s) - i - 1] and s[len(s) - i - 1] <= "Z":
      position = (len(s) - i - 1)
   i = i + 1

print position
