#!/usr/bin/env python3

'''Remove first and last characters from a string'''

import sys

def chop(s):
   return s[1:len(s) - 1]

def main():
   for line in sys.stdin:
      chopped = chop(line.strip())
      if len(chopped) > 0:
         print(chopped)

if __name__ == '__main__':
   main()
