#!/usr/bin/env python3

import sys

def anagram(left, right):
   if sorted(left) == sorted(right):
      return True
   else:
      return False

def main():
   for line in sys.stdin:
      [left, right] = line.split()
      print(anagram(left, right))

if __name__ == '__main__':
   main()
