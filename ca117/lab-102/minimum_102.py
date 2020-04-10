#!/usr/bin/env python3

def minimum(ns):
    if len(ns) == 1:
        return ns[0]
    m = minimum(ns[1:])
    if ns[0] < m:
        return ns[0]
    return m

def main():
    min = None
    print(minimum([6, 5, 1, 3, 4]))
    print(minimum([6, 5, 11, 3, 4]))
    print(minimum([6, 15, 11, 13, 14]))
    print(minimum([6, 15, 11, 13, 4]))

if __name__ == '__main__':
    main()
