#!/usr/bin/env python

curr = input()

i = 0
while i < 5:
   prev = curr
   curr = input()
   if prev < curr:
      print "higher"
   elif curr < prev:
      print "lower"
   else:
      print "equal"
   i = i + 1
