#!/usr/bin/env python

## Assume existing integer variables n and m.
## One is odd, and the other is even.
## when run, creates a new variable named odd
## containing only the value of the odd variable.

## Remainder for even number is 0, multiplied by variable is 0.
## Remainder for odd number is 1, multiplied by variable is
## still the original variable.

odd = (n * (n % 2)) + (m * (m % 2))

# print(odd)
