#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
   curr = files[i]

   with open(curr) as f:
      if curr[len(curr) - 3:] == ".py" and f.read(1):
         print curr
      elif f.read(21) == "#!/usr/bin/env python":
         print curr

   i = i + 1
