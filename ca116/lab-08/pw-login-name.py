#!/usr/bin/env python

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[i] != ":":
      i = i + 1

   user = s[:i]
   print user

   s = raw_input()
