#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   integer = int(s)
   a.append(integer)
   s = raw_input()

i = 0
while i < len(a):

   smallest = i
   
   j = i + 1
   while j < len(a):
      if a[j] < a[smallest]:
         smallest = j
      j = j + 1

   tmp = a[i]
   a[i] = a[smallest]
   a[smallest] = tmp

   i = i + 1

i = 0
while i < len(a):
   print a[i]
   i = i + 1
