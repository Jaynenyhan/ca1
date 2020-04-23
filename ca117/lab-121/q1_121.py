#!/usr/bin/env python3

import sys

# rotate string anticlockwise by n steps
def rotate(s, n):
    m = n % len(s)
    return s[m:] + s[:m]

def main():
    s = sys.argv[1]
    n = int(sys.argv[2])
    print(rotate(s, n))

if __name__ == "__main__":
    main()
