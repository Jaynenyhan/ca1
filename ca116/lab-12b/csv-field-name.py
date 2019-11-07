#!/usr/bin/env python

import sys

# Get inputs
n = int(sys.argv[1])
s = raw_input()

# Find nth comma
start = 0
i = 0
while i < n:
   while start < len(s) and s[start] != ",":
      start = start + 1
   start = start + 1  # Start of word instead of comma
   i = i + 1

# Find (n + 1)th comma
end = start
while end < len(s) and s[end] != ",":
   end = end + 1

print s[start:end]
