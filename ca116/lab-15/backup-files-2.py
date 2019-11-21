#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
   curr = files[i]

   if os.path.isfile(curr) and curr[len(curr) - 4:] != ".bak":
         with open(curr) as f:
            with open(curr + ".bak", "w") as fw:
               fw.write(f.read())

   i = i + 1
