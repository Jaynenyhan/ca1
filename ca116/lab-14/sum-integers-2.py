#!/usr/bin/env python

import sys

file_name = sys.argv[1]
with open(file_name) as fd:
   ns = fd.readlines()

total = 0
i = 0
while i < len(ns):
   n = int(ns[i])
   total = total + n
   i = i + 1

print total
