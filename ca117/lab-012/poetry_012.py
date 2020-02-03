#!/usr/bin/env python3

import sys

def centre(s, maxlen):
   print('{:^{}s}'.format(s, maxlen))

def main():
   lines = []
   maxlen = 0
   for line in sys.stdin:
      s = line.strip()
      if len(s) > maxlen:
         maxlen = len(s)
      lines.append(s)
   for line in lines:
      centre(line, maxlen)

if __name__ == '__main__':
   main()
