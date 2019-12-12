#!/usr/bin/env python

n = 20
import sys

# Getting input
points = {}
lines = sys.stdin.readlines()
i = 0
while i < len(lines):
   tokens = lines[i].split()
   key = "-".join(tokens)
   points[key] = True
   i += 1

# Should we plot given point
def should_plot(x, y):
   key = str(x) + "-" + str(y)
   return key in points

# Printing graph
print " " + "-" * n

i = 0
while i < n:
   y = n - i - 1
   line = ""
   x = 0
   while x < n:
      if should_plot(x, y):
         line = line + "*"
      else:
         line = line + " "
      x += 1

   print "|" + line + "|"
   i += 1

print " " + "-" * n