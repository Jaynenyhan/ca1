#!/usr/bin/env python

import sys

german = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

numbers = sys.stdin.readlines()
i = 0
while i < len(numbers):
   number = numbers[i].rstrip()
   if number in german:
      print german[number]
   i += 1
