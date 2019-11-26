#!/usr/bin/env python

import sys

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

words = sys.stdin.readlines()
i = 0
while i < len(words):
   word = words[i].rstrip()
   if word in fruit:
      print word
   i += 1
