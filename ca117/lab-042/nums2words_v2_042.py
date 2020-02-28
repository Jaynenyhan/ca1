#!/usr/bin/env python3

import sys

def nums2words(s):
    # key = int, val = str
    d = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'
    }
    # make list of words
    ns = s.split()
    # i = index of list, n = element in list
    for i, n in enumerate(ns):
        # replace list element with dict equivalent
        # if list element not in dict, unknown
        try:
            ns[i] = d[int(n)]
        except (ValueError, KeyError):
            ns[i] = 'unknown'
    # join with spaces and return
    return " ".join(ns)

def main():
    for line in sys.stdin:
        print(nums2words(line))

if __name__ == '__main__':
    main()
