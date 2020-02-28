#!/usr/bin/env python3

import sys

def main():
    # init count
    d = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    # start counting
    for ch in sys.stdin.read():
        s = ch.lower()
        if s in 'aeiou':
            d[s] += 1
    # get len of longest int
    v_len = len(str(max(d.values())))
    # sorted by value, descending order
    for k in sorted(d, key=d.get, reverse=True):
        print('{} : {:>{:d}d}'.format(k, d[k], v_len))

if __name__ == '__main__':
    main()
