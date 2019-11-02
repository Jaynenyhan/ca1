#!/usr/bin/env python

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[i:i + 2] != "WI":
      i = i + 1

   if s[i:i + 2] == "WI":
      print s[:i - 1]

   s = raw_input()
