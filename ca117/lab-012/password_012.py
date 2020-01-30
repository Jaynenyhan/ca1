#!/usr/bin/env python3

import sys

def password(s):
   upper = 0
   lower = 0
   digit = 0
   other = 0
   for c in s:
      if c.isupper():
         upper = 1
      elif c.islower():
         lower = 1
      elif c.isdigit():
         digit = 1
      else:
         other = 1
   return upper + lower + digit + other


def main():
   for line in sys.stdin:
      s = line.strip()
      print(password(s))

if __name__ == '__main__':
   main()
