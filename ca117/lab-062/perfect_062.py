#!/usr/bin/env python3

import sys

def sumFac(n):
    return sum([i for i in range(1, n // 2 + 1) if n % i == 0])

def isPerfect(n):
    if n == sumFac(n):
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        n = int(line.strip())
        print(isPerfect(n))

if __name__ == '__main__':
    main()
