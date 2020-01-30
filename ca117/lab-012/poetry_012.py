#!/usr/bin/env python3

import sys

def centre(s, maxlen):
   print('{:^{}s}'.format(s, maxlen))

def main():
   maxlen = 0
   for line in sys.stdin:
      s = line.strip()
      if len(s) > maxlen:
         maxlen = len(s)
   for line in sys.stdin:
      s = line.strip()
      centre(s, maxlen)

if __name__ == '__main__':
   main()
