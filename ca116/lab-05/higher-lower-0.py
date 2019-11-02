#!/usr/bin/env python

curr = input()

while curr != 0:
   prev = curr
   curr = input()
   if curr != 0:
      if prev < curr:
         print "higher"
      elif curr < prev:
         print "lower"
      else:
         print "equal"
