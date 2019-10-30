#!/usr/bin/env python

n = input()

## 0, 1, 2, 3, 4 => 0, -1, 2, -3, 4, -5
## odds are negative, evens are positive

i = 0
while i < n:
   if i % 2 == 0:
      print i
   elif i % 2 != 0:
      print -i
   i = i + 1
