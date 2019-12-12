#!/usr/bin/env python

import sys
args = sys.argv[1:]

total = 0
i = 0
while i < len(args):
   file_name = args[i]
   with open(file_name) as fd:
      ns = fd.readlines()

   j = 0
   while j < len(ns):
      n = int(ns[j])
      total += n
      j += 1

   i += 1

print total
