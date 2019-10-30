#!/usr/bin/env python

bin = ""
n = input()

while n != 0:
   bin = str(n % 2) + bin
   n = n / 2

print bin
