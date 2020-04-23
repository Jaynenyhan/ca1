#!/usr/bin/env python3

import sys

# print index where integers in lists match
def matching(ns1, ns2):
    matches = []
    for i in range(0, len(ns1)):
        if ns1[i] == ns2[i]:
            matches.append(i)
    return matches

def main():
    lines = sys.stdin.readlines()
    ns1 = lines[0].split()
    ns2 = lines[1].split()
    print(matching(ns1, ns2))

if __name__ == "__main__":
    main()
