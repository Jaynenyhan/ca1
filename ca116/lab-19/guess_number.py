#!/usr/bin/env python

import secret_number
n = 1000

def play():
   i = 0
   while i < n and secret_number.guess(i) != "correct":
      i = i + 1
   return i


print play()
