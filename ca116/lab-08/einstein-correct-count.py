#!/usr/bin/env python

count = 0

s = raw_input()
while s != "end":

   i = 0
   while i < len(s) and s[len(s) - i - 1:] != "correct":
      i = i + 1

   if s[len(s) - i - 3:] != "incorrect" and s[len(s) - 2:] != "py":
      count = count + 1

   s = raw_input()

print count
