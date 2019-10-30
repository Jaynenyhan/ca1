#!/usr/bin/env python

i = 0
while i < 10:
   s = raw_input()
   i = i + 1

   j = 0
   while j < len(s) and s[j] != "+":
      j = j + 1

   number1 = int(s[:j])
   number2 = int(s[j + 1:])
   print number1 + number2
