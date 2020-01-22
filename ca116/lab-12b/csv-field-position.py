#!/usr/bin/env python

import sys

# Get inputs
arg = sys.argv[1]
s = raw_input()

# Count commas while passing
count = 0
i = 0
while i < len(s) and s[i:i + len(arg)] != arg:
   if s[i] == ",":
      count += 1
   i += 1

print count
