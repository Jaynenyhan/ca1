#!/usr/bin/env python3

import sys

def clock(n, m):
    if n == int(n):
        print('yes')

def main():
    n, m = [int(x) for x in sys.stdin.read().split()]
    clock(n, m)

if __name__ == "__main__":
    main()
