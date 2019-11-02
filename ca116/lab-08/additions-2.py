#!/usr/bin/env python

total = 0
start = 0
end = 0

s = raw_input()

i = 0
while i < 5:
   end = start
   while end < len(s) and s[end] != "+":
      end = end + 1

   integer = int(s[start:end])
   total = total + integer

   start = end + 1
   i = i + 1

print total
