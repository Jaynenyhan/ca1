#!/usr/bin/env python

import sys

words = sys.stdin.readlines()
fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

i = 0
while i < len(words):
   word = words[i].rstrip()
   if word in fruit:
      print word
   i += 1
