#!/usr/bin/env python

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[len(s) - i - 1] != "/":
      i = i + 1

   taskname = s[len(s) - i:]

   suffix = s[len(s) - 2:]
   if suffix == "py":
      print taskname

   s = raw_input()
