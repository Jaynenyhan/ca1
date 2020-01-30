#!/usr/bin/env python3

import sys

def conv2decimal(number, base):
   number_reversed = number[::-1]
   result = 0
   i = 0
   while i < len(number_reversed):
      result = result + int(number_reversed[i]) * int(base) ** i
      i += 1
   return result

def main():
   for line in sys.stdin:
      s = line.split()
      output = conv2decimal(s[0], s[1])
      print(output)

if __name__ == '__main__':
   main()
