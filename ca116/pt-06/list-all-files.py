#!/usr/bin/env python

import os

dirs = ["."]

while 0 < len(dirs):
   directory = dirs.pop()
   entries = os.listdir(directory)
   i = 0
   while i < len(entries):
      path = directory + "/" + entries[i]
      if os.path.isfile(path):
         print path
      elif os.path.isdir(path):
         dirs.append(path)
      i = i + 1

