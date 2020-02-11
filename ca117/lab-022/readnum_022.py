#!/usr/bin/env python3

import sys

def readnum(lines):
   for line in lines:
      s = line.strip()
      try:
         n = int(s)
         print('Thank you for {}'.format(n))
         return
      except ValueError:
         print('{} is not a number'.format(s))

def main():
   readnum(sys.stdin.readlines())

if __name__ == '__main__':
   main()
