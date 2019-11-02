#!/usr/bin/env python

lines = []

s = raw_input()
while s != "end":

   i = 0
   while i < len(lines) and lines[i] != s:
      i = i + 1

   if i < len(lines):
      lines = lines
   else:
      lines.append(s)
      print s

   s = raw_input()
