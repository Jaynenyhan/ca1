#!/usr/bin/env python

n = input()
curr = 0
prev = 0

i = 0
while curr + prev < n:
   if i == 0:
      print 0
      prev = 0
   elif i == 1:
      print 1
      curr = 1
   else:
      prevprev = prev
      prev = curr
      curr = prevprev + prev
      print curr
   i = i + 1
