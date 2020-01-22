#!/usr/bin/env python

import sys

# Get inputs
lines = sys.stdin.read().split()

# Split each line and print last element
i = 0
while i < len(lines):
   curr = lines[i].split("/")
   print curr[len(curr) - 1]
   i += 1
