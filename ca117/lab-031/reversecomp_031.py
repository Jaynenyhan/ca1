#!/usr/bin/env python3

import sys

def reversecomp(a):
    words = [s.strip() for s in a]
    atleast_5_letters = [s for s in words if len(s) >= 5]
    atleast_5_letters_lower = set([s.lower() for s in atleast_5_letters])
    reverse_words = [s for s in atleast_5_letters if s[::-1].lower() in atleast_5_letters_lower]
    print(reverse_words)

def main():
   reversecomp(sys.stdin.readlines())

if __name__ == '__main__':
   main()
