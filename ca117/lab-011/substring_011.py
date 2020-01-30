#!/usr/bin/env python3

import sys

def substring(s1, s2):
   s1 = s1.lower()
   s2 = s2.lower()
   if s1 in s2:
      return True
   else:
      return False

def main():
   for line in sys.stdin:
      s = line.split()
      output = substring(s[0], s[1])
      print(output)

if __name__ == '__main__':
   main()
