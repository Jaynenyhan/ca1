#!/usr/bin/env python3

import sys

def main():
    d = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    for ch in sys.stdin.read():
        s = ch.lower()
        if s in 'aeiou':
            d[s] += 1
    v_len = len(str(d[max(d, key=d.get)]))
    for k in sorted(d, key=d.get, reverse=True):
        print('{} : {:>{:d}d}'.format(k, d[k], v_len))

if __name__ == '__main__':
    main()
