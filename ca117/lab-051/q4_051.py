#!/usr/bin/env python3

import sys

def mean(a):
    return sum(a) / len(a)

def median(a):
    a.sort()
    n = len(a) // 2
    if len(a) % 2 == 0:
        return (a[n] + a[n - 1]) / 2
    else:
        return a[n]


def main():
    a = [int(s.strip()) for s in sys.stdin.readlines()]
    print('Mean: {:.1f}\nMedian: {:.1f}'.format(mean(a), median(a)))

if __name__ == '__main__':
    main()
