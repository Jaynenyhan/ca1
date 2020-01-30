#!/usr/bin/env python3

import sys

def substring(s1, s2):
   if s1.lower() in s2.lower():
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
