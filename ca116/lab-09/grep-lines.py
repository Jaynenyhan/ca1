#!/usr/bin/env python

import sys
args = sys.argv[1:]
a = []

s = raw_input()
while s != "end":
   a.append(s)
   s = raw_input()

print args