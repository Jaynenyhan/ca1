#!/usr/bin/env python3

import sys

def simple(s):
    # add unique chars to list
    chars = []
    for ch in s:
        if ch not in chars:
            chars.append(ch)
    # deletions required
    if len(chars) > 2:
        return len(chars) - 2
    else:
        return 0

def main():
    for line in sys.stdin:
        s = line.strip()
        print (simple(s))

if __name__ == "__main__":
    main()
