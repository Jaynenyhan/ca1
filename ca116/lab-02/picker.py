#!/usr/bin/env python

a = input()
b = input()
c = input()

## a - c is even
## b - c is odd.

print (a * ((c + 1) % 2)) + (b * (c % 2))
