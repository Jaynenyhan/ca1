#!/usr/bin/env python

total = 0

while total != 1000:
   s = raw_input()

   i = 0
   while i < len(s) and s[i] != "+":
      i = i + 1

   integer1 = int(s[:i])
   integer2 = int(s[i + 1:])
   total = integer1 + integer2

   print total
