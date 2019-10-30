#!/usr/bin/env python

x1 = input()
y1 = input()
r1 = input()

x2 = input()
y2 = input()
r2 = input()

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))
add_radius = (r1 + r2) ** 2

if add_radius > distance:
   print "yes"
else:
   print "no"
