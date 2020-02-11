#!/usr/bin/env python3

import sys

def prime(n):
   if n > 1:
      for i in range(2, n):
         if (n % i) == 0:
            return False
      else:
         return True

def numcomps(n):
   a = list(range(1, n + 1))

   print('Multiples of 3: {}'.format([x for x in a if x % 3 == 0]))
   print('Multiples of 3 squared: {}'.format([x * x for x in a if x % 3 == 0]))
   print('Multiples of 4 doubled: {}'.format([x * 2 for x in a if x % 4 == 0]))
   print('Multiples of 3 or 4: {}'.format([x for x in a if x % 3 == 0 or x % 4 == 0]))
   print('Multiples of 3 and 4: {}'.format([x for x in a if x % 12 == 0]))
   print('Multiples of 3 replaced: {}'.format(['X' if x % 3 == 0 else x for x in a]))
   print('Primes: {}'.format([x for x in a if prime(x)]))

def main():
   n = int(sys.argv[1])
   numcomps(n)

if __name__ == '__main__':
   main()
