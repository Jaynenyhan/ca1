#!/usr/bin/env python3

from priority_queue_112 import PQ
import sys

def main():
    pq = PQ()
    # add all ints to a pq
    for line in sys.stdin:
        pq.insert(int(line.strip()))
    # remove biggest until we have the n minimum numbers, n is arg
    while int(sys.argv[1]) != pq.size():
        pq.delMax()
    # print the n numbers
    while pq.size() != 0:
        print(pq.delMax())

if __name__ == '__main__':
    main()
