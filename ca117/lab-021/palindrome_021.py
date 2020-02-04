#!/usr/bin/env python3

import sys

def palindrome(s):
   chars_only = ""
   for c in s:
      if c.isalnum():
         chars_only += c
   chars_only = chars_only.lower()
   if chars_only == chars_only[::-1]:
      return True
   else:
      return False

def main():
   for line in sys.stdin:
      print(palindrome(line))

if __name__ == '__main__':
   main()
