#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
   curr = files[i]
   if curr[len(curr) - 3:] == ".py":

      with open(curr) as f:
         if f.read(1):
            print curr

   i = i + 1
