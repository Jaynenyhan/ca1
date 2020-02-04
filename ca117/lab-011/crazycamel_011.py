#!/usr/bin/env python3

import sys

def camel(s):
   new_words = []
   for word in s.split():
      new_words.append(word[:-1] + word[-1].upper())
   new_string = " ".join(new_words)
   print(new_string)

def main():
   for line in sys.stdin:
      camel(line)

if __name__ == '__main__':
   main()
