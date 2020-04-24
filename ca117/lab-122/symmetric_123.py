#!/usr/bin/env python3

import sys

def sym(strs):
    # first half
    first_half = []
    for i in range(0, len(strs), 2):
        s = strs[i]
        first_half.append(s)
    # second hald
    second_half = []
    for i in range(1, len(strs), 2):
        s = strs[i]
        second_half.append(s)
    # return second half in reverse
    out = first_half + second_half[::-1]
    return '\n'.join(out)

def main():
    names = [s.strip() for s in sys.stdin.readlines()]
    print(sym(names))

if __name__ == "__main__":
    main()
