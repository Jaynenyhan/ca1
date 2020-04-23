#!/usr/bin/env python3

import sys

def average(ns):
    return sum(ns) / len(ns)

def sorter(kv):
    return kv[1]

def lines2scores(lines):
    d = {}
    for line in lines:
        name, scores = line.split(':')
        scores = [int(score) if score != 'X' else 0 for score in scores.lstrip().split(',')]
        d[name] = average(scores)
    return d

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    d = lines2scores(lines)
    for (k, v) in sorted(d.items(), key=sorter, reverse=True):
        print('{}: {:.1f}'.format(k, v))

if __name__ == "__main__":
    main()
