#!/usr/bin/env python3

import sys

def square(points):
    a = points[0]
    b = points[1]
    c = points[2]
    distance_ab = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    distance_ac = ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) ** 0.5
    if distance_ab > distance_ac:
        point = c
    elif distance_ac > distance_ab:
        point = b
    else:
        point = a
    a_dist_from_point = [a[0] - point[0], a[1] - point[1]]
    b_dist_from_point = [b[0] - point[0], b[1] - point[1]]
    c_dist_from_point = [c[0] - point[0], c[1] - point[1]]
    if a_dist_from_point != [0, 0] and c_dist_from_point != [0, 0]:
        x = a_dist_from_point[0] + c[0]
        y = a_dist_from_point[1] + c[1]
    elif a_dist_from_point != [0, 0] and b_dist_from_point != [0, 0]:
        x = a_dist_from_point[0] + b[0]
        y = a_dist_from_point[1] + b[1]
    elif b_dist_from_point != [0, 0] and c_dist_from_point != [0, 0]:
        x = b_dist_from_point[0] + c[0]
        y = b_dist_from_point[1] + c[1]
    print(x, y)

def main():
    points = []
    for line in sys.stdin:
        tokens = line.split()
        points.append([int(tokens[0]), int(tokens[1])])
    square(points)

if __name__ == '__main__':
    main()
