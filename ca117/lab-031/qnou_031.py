#!/usr/bin/env python3

import sys

def compare(s):
   s = s.lower()
   for i in range(len(s)):
      if s[i] == 'q':
         if i == len(s):
            return True
         elif s[i + 1] != 'u':
            return True
   return False

def qnou(a):
   a = [s.strip() for s in a]
   print('Words with q but no u: {}'.format([s for s in a if compare(s)]))

def main():
   qnou(sys.stdin.readlines())

if __name__ == '__main__':
   main()
