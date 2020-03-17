#!/usr/bin/env python3

import sys

def stars(lines, n):
    count = 0
    chars = [ch for ch in "".join(lines)]
    i = 0
    while i < len(chars):
        if chars[i] == "-":
            count += 1
            while i < len(chars) and chars[i] == "-":
                if i + n < len(chars) and chars[i + n] == "-":
                    i = i + n
                elif i < len(chars) and chars[i] == "-":
                    i += 1
        i += 1
    return count

def main():
    lines = sys.stdin.readlines()
    m, n = int(lines[0].split()[0]), int(lines[0].split()[1]) + 1
    print(stars(lines[1:], n))

if __name__ == '__main__':
    main()
