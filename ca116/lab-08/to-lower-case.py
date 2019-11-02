#!/usr/bin/env python

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"
t = ""

s = raw_input()
while s != "end":

   i = 0
   while i < len(s):

      if "A" <= s[i] and s[i] <= "Z":
         j = 0
         while upper[j] != s[i]:
            j = j + 1
         t = t + lower[j]

      else:
         t = t + s[i]

      i = i + 1

   print t
   t = ""

   s = raw_input()
