#!/usr/bin/env python

n = input()

## Fib = sum of 2 prev numbers
## X(n+2)= X(n+1) + Xn
## 2+2 = 2+1+2

i = 0
while i < n:
   if i == 0:
      print 0
      prev = 0
   elif i == 1:
      print 1
      current = 1
   else:
      prevprev = prev
      prev = current
      current = prevprev + prev
      print current
   i = i + 1
