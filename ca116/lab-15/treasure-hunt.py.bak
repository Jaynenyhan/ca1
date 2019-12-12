#!/usr/bin/env python

import os
file_name = "start.txt"

with open(file_name) as f:
   contents = f.read()

while contents[len(contents) - 5:] == ".txt\n":

   file_name = contents[:len(contents) - 1]
   with open(file_name) as f:
      contents = f.read()

print contents[:len(contents) - 1]
