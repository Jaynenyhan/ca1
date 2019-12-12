#!/usr/bin/env python

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

translation = {}
i = 0
while i < len(src):
   translation[src[i]] = dst[i]
   i += 1

lines = sys.stdin.readlines()
print lines
t = ""
i = 0
while i < len(lines):
   if lines[i] in src:
      t = t + translation[lines[i]]
   else:
      t = t + lines[i]
   i += 1

print t
