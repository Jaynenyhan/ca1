#!/usr/bin/env python

import sys
lines = sys.stdin.read().split()

seen = {}
i = 0
while i < len(lines) and lines[i] not in seen:
   curr = lines[i]
   seen[curr] = "True"
   i += 1

if i < len(lines):
   print "snap:", lines[i]
