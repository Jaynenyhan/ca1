#!/usr/bin/env python3

import sys
from string import punctuation

def main():
    words = [''.join(ch for ch in s if ch not in punctuation.replace("'", "")).lower() for s in sys.stdin.read().split()]
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    for k in sorted(d):
        print('{} : {}'.format(k, d[k]))

if __name__ == '__main__':
    main()
