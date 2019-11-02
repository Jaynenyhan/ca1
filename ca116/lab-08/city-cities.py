#!/usr/bin/env python

# To strip first line
s = raw_input()

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[i:i + 5] != "City,":
      i = i + 1

   if s[i:i + 5] == "City,":
      print s[:i + 4]

   s = raw_input()
