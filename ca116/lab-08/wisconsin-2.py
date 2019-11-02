#!/usr/bin/env python

count = 0

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[i:i + 2] != "WI":
      i = i + 1

   if s[i:i + 2] == "WI":
      count = count + 1

   s = raw_input()

print count
