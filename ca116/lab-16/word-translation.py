#!/usr/bin/env python

import sys

translations = {}
with open("translation.txt") as f:
   pairs = f.read().split()
   i = 0
   while i < len(pairs):
      translations[pairs[i]] = pairs[i + 1]
      i += 2

numbers = sys.stdin.readlines()
i = 0
while i < len(numbers):
   number = numbers[i].rstrip()
   if number in translations:
      print translations[number]
   i += 1
