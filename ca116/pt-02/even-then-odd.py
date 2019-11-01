#!/usr/bin/env python

odd_numbers = []

s = raw_input()
while s != "end":
   n = int(s)
   if n % 2 == 0:
      print n
   else:
      odd_numbers.append(n)
   s = raw_input()

i = 0
while i < len(odd_numbers):
   print odd_numbers[i]
   i = i + 1
