#!/usr/bin/env python3

import sys

def count_e(s):
   return s.lower().count('e')

def most_e(a):
   max_e = max([s for s in a if 'e' in s.lower()], key=count_e).count('e')
   return [s for s in a if s.lower().count('e') == max_e]

def wordcomps(a):
   a = [s.strip() for s in a]
   print('Words containing 17 letters: {}'.format([s for s in a if len(s) == 17]))
   print('Words containing 18+ letters: {}'.format([s for s in a if len(s) > 17]))
   print('Shortest word containing all vowels: {}'.format(min([s for s in a if all(x in s for x in 'aeiou')], key=len)))
   print('Words with 4 a\'s: {}'.format([s for s in a if s.lower().count('a') == 4]))
   print('Words with 2+ q\'s: {}'.format([s for s in a if s.lower().count('q') > 1]))
   print('Words containing cie: {}'.format([s for s in a if 'cie' in s]))
   print('Anagrams of angle: {}'.format([s for s in a if s != 'angle' and sorted(s.lower()) == sorted('angle')]))
   print('Words ending in iary: {}'.format(len([s for s in a if s[-4:] == 'iary'])))
   print('Words with most e\'s: {}'.format(most_e(a)))

def main():
   wordcomps(sys.stdin.readlines())

if __name__ == '__main__':
   main()
