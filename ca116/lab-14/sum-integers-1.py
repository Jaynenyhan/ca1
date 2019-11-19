#!/usr/bin/env python

import sys
ns = sys.stdin.read().split()

total = 0
i = 0
while i < len(ns):
   n = int(ns[i])
   total = total + n
   i = i + 1

print total
