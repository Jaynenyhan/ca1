#!/usr/bin/env python3

import sys
import math

def square(points):
    p1 = points[0]
    p2 = points[1]
    p3 = points[2]
    distance1 = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    distance2 = math.sqrt(((p1[0] - p3[0]) ** 2) + ((p1[1] - p3[1]) ** 2))
    if distance1 > distance2:
        diagonal1 = p1
        diagonal2 = p2
        other = p3
    else:
        diagonal1 = p1
        diagonal2 = p3
        other = p2
    print(diagonal1)
    print(diagonal2)

def main():
    points = []
    for line in sys.stdin:
        tokens = line.split()
        points.append([int(tokens[0]), int(tokens[1])])
    square(points)

if __name__ == '__main__':
    main()
