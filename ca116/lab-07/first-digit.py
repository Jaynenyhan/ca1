#!/usr/bin/env python

s = raw_input()

# Test whether s[i] is a digit.
#"0" <= s[i] and s[i] <= "9"

# Test whether s[i] is not a digit.
#s[i] < "0" or "9" < s[i]

# while i < N and not P

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
   i = i + 1

if i < len(s):
   print s[i], i
