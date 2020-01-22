#!/usr/bin/env python

import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1) as f1:
   lines1 = f1.readlines()
with open(filename2) as f2:
   lines2 = f2.readlines()

# compare i-th lines 
i = 0
while i < len(lines1) or i < len(lines2):
   line1 = lines1[i]
   line2 = lines2[i]
   j = 0
   while j < len(line1) or j < len(line2):
      if line1[j] != line2[j]:
         print i, j
      j += 1
   i += 1
