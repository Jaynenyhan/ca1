#!/usr/bin/env python3

def maximum(ns):
    if len(ns) == 1:
        return ns[0]
    m = maximum(ns[1:])
    if ns[0] > m:
        return ns[0]
    return m

def main():
    max = None
    print(maximum([6, 5, 1, 3, 4]))
    print(maximum([6, 5, 11, 3, 4]))
    print(maximum([6, 15, 11, 13, 14]))
    print(maximum([6, 15, 11, 13, 4]))

if __name__ == '__main__':
    main()
