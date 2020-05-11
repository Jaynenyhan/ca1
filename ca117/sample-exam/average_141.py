#!/usr/bin/env python3

import sys

def word2len(words):
    d = {}
    for word in words:
        d[word] = len(word)
    return d

def averagelen(d):
    vals = [v for _, v in d.items()]
    average = sum(vals) / len(vals)
    return average

def main():
    words = sys.stdin.read().split()
    d = word2len(words)
    average = averagelen(d)
    print('Average: {:.2f}'.format(average))
    for word in words:
        if d[word] > average:
            print(word)

if __name__ == "__main__":
    main()
