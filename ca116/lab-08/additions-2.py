#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and s[i] != "+":
   i = i + 1
   print "i:", i

   j = i + 1
   while j < len(s) and s[j] != "+":
      j = j + 1
      print "j:", j