#!/usr/bin/env python

w = raw_input()

i = 0
while i < len(w) / 2 and w[i] == w[len(w) - i - 1]:
   i = i + 1

if i == len(w) / 2:
   print "palindrome"
