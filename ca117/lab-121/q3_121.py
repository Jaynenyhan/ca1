#!/usr/bin/env python3

import sys

# if word contains aeiou in that order, print
def aeiou(s):
    chars = [ch.lower() for ch in s if ch.lower() in list('aeiou')]
    if chars == list('aeiou'):
        print(s)

def main():
    for line in sys.stdin:
        s = line.strip()
        aeiou(s)

if __name__ == "__main__":
    main()
