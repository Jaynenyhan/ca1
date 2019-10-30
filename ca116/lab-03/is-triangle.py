#!/usr/bin/env python

a = input()
b = input()
c = input()

if a + b <= c or b + c <= a or a + c <= b:
   print "no"
else:
   print "yes"
