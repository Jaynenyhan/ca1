#!/usr/bin/env python

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[i] != ":":
      i = i + 1
   user = s[:i]

   i = 0
   while i < len(s) and s[len(s) - i - 1] != ":":
      i = i + 1
   shell = s[len(s) - i:]

   print user, shell

   s = raw_input()
