#!/usr/bin/env python

s = raw_input()

start = 0
end = 0
count = 0

while count < 2:
   start = end
   while start < len(s) and ("0" > s[start] or s[start] > "9"):
      start = start + 1
   end = start
   while end < len(s) and ("0" <= s[end] and s[end] <= "9"):
      end = end + 1
   count = count + 1

if start < len(s):
   print s[start:end], start
