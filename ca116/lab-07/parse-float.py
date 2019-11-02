#!/usr/bin/env python

f = raw_input()

i = 0
while i < len(f) and f[i] != ".":
   i = i + 1

integer = f[:i]
fraction = f[i + 1:]

print integer
print fraction
