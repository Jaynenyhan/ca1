#!/usr/bin/env python3

import sys
from string import punctuation

def main():
    # get list of words, minus punctuation (except apostrophes), in lowercase
    words = [''.join(ch for ch in s if ch not in punctuation.replace("'", "")).lower() for s in sys.stdin.read().split()]
    # generate dict counting the words
    count = {}
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    # dict comprehension to meet q's requirements
    d = {k: v for (k, v) in count.items() if len(k) > 3 and v > 2}
    # get len of longest str and int
    k_len = len(max(d, key=len))
    v_len = len(str(d[max(d, key=d.get)]))
    # printing
    for k in sorted(d):
        print('{:>{:d}s} : {:{:d}d}'.format(k, k_len, d[k], v_len))

if __name__ == '__main__':
    main()
