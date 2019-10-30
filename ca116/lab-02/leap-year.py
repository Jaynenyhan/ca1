#!/usr/bin/env python

year = input()

## div by 400
## div by 4
## not div by 100

print year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
