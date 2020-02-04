#!/usr/bin/env python3

import sys

def unique_count(a):
   words = []
   for s in a:
      t = ""
      for c in s:
         if c.isalnum():
            t += c
      if t != "":
         t = t.lower()
         if t not in words:
            words.append(t)
   print(len(words))

def main():
   unique_count(sys.stdin.read().split())

if __name__ == '__main__':
   main()
