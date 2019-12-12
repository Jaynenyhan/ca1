#!/usr/bin/env python

import sys

a = sys.stdin.read().split("/")

i = 0
while i < len(a):
   if "." in a[i]:
      print a[i]
   i += 1