#!/usr/bin/env python3

import sys

def evil(s):
    if [c for c in s.lower() if c in 'evil'] == list('evil'):
        print(s)

def main():
    for line in sys.stdin:
        s = line.strip()
        evil(s)

if __name__ == '__main__':
    main()
