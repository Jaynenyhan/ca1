#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point: ({:.1f}, {:.1f})'.format(self.x, self.y)

    def midpoint(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)

class Circle(object):

    def __init__(self, c=Point(), r=0):
        self.centre = c
        self.radius = r

    def __str__(self):
        return 'Centre: ({:.1f}, {:.1f})\nRadius: {:d}'.format(
            self.centre.x, self.centre.y, self.radius)

    def __add__(self, other):
        mid = Point.midpoint(self.centre, other.centre)
        r = self.radius + other.radius
        return Circle(Point(mid.x, mid.y), r)

def main():
    p1 = Point()
    p2 = Point(4, 6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10, 10)
    c4 = Circle(p3, 15)
    c5 = c2 + c4
    print(c5)

if __name__ == '__main__':
    main()
