#!/usr/bin/env python

import sys
args = sys.argv[1:]

count = 0

i = 0
while i < len(args):
   count = count + int(args[i])
   i = i + 1

print count
