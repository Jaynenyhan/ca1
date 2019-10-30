#!/usr/bin/env python

n = input()
t = ""

i = 0
while i < n:
   m = input()
   if i == n - 1:
      t = t + ("*" * m)
   else:
      t = t + ("*" * m) + "\n"
   i = i + 1
print t
