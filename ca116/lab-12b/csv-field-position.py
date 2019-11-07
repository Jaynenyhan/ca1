#!/usr/bin/env python

import sys

# Get inputs
arg = sys.argv[1]
s = raw_input()

print arg

i = 0
while i < len(s) and s[i:len(arg)] != arg:
   print i
   print s[i:len(arg)]
   i = i + 1

print s[i:len(arg)]