#!/usr/bin/env python

a = raw_input()
b = raw_input()
c = raw_input()

al = len(a)
bl = len(b)
cl = len(c)

if al > bl and al > cl:
   print a
elif bl > al and bl > cl:
   print b
elif cl > al and cl > bl:
   print c
