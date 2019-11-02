#!/usr/bin/env python

import sys
args = sys.argv[1]

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[i:i + len(args)] != args:
      i = i + 1

   if s[i:i + len(args)] == args:
      print s

   s = raw_input()
