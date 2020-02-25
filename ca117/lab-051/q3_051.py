#!/usr/bin/env python3

import sys

def caps(s):
    for c in s:
        if c.islower():
            s = s.replace(c, ' ')
    caps_list = s.split()
    return max(caps_list, key=len)

def main():
    for line in sys.stdin:
        s = line.strip()
        print(caps(s))

if __name__ == '__main__':
    main()
