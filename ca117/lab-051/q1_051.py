#!/usr/bin/env python3

import sys

def swap_adj_chars(s):
    return ''.join([s[i:i + 2][::-1] for i in range(0, len(s), 2)])

def main():
    s = sys.argv[1]
    print(swap_adj_chars(s))

if __name__ == '__main__':
    main()
