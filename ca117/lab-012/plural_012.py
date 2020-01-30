#!/usr/bin/env python3

import sys

def plural(s):
   es = ["ch", "sh", "x", "s", "z", "o"]
   vowels = ["a", "e", "i", "o", "u"]
   if s[-2:] in es or s[-1] in es:
      return s + "es"
   elif s[-2] not in vowels and s[-1] == "y":
      return s[:-1] + "ies"
   elif s[-1] == "f":
      return s[:-1] + "ves"
   elif s[-2:] == "fe":
      return s[:-2] + "ves"
   else:
      return s + "s"

def main():
   for line in sys.stdin:
      s = line.strip()
      print(plural(s))

if __name__ == '__main__':
   main()
