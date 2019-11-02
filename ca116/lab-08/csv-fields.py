#!/usr/bin/env python

s = raw_input()

start = 0
end = 0

while end < len(s):
   end = start
   while end < len(s) and s[end] != ",":
      end = end + 1

   word = s[start:end]
   print word

   start = end + 1
