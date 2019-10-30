#!/usr/bin/env python

pos = 0
neg = 0

i = 0
while i < 5:
   n = input()
   if n < 0:
      neg = neg + n
   else:
      pos = pos + n
   i = i + 1

print neg, pos
