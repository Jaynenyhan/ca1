#!/usr/bin/env python

a = input()
b = input()
c = input()

## a if c is even
## b if c is odd.

print (a * ((c + 1) % 2)) + (b * (c % 2))
