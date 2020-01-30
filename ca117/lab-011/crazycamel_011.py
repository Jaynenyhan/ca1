#!/usr/bin/env python3

import sys

def camel(line):
   new_words = []
   for word in line.split():
      new_words.append(word[:-1] + word[-1].upper())
   new_string = " ".join(new_words)
   return new_string

def main():
   for line in sys.stdin:
      output = camel(line)
      print(output)

if __name__ == '__main__':
   main()
