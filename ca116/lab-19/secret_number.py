#!/usr/bin/env python

secret = 666

def guess(n):
   if n == secret:
      return "correct"
   elif n < secret:
      return "too-low"
   elif n > secret:
      return "too-high"
