#!/usr/bin/env python3

import sys

def middle(s):
   if len(s) % 2 == 1:
      calc = len(s) // 2
      return s[calc]
   else:
      return "No middle character!"

def main():
   for line in sys.stdin:
      s = line.strip()
      output = middle(s)
      print(output)

if __name__ == '__main__':
   main()
