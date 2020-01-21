#!/usr/bin/env python

import sys

# Get inputs
n = int(sys.argv[1])

# First half
i = 0
while i < n / 2 + 1:
   spaces = (n / 2) - i
   stars = n - spaces * 2
   print " " * spaces + "*" * stars
   i += 1

# Bring i back to before the largest line
i -= 2

# Second half
while i >= 0:
   spaces = (n / 2) - i
   stars = n - spaces * 2
   print " " * spaces + "*" * stars
   i -= 1
