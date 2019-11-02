#!/usr/bin/env python

n = input()
hex_number = ""
hexs = "0123456789abcdef"

while n != 0:
   hex_number = hexs[n % 16] + hex_number
   n = n / 16

print hex_number
