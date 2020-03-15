#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** 0.5

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)

class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        return Point(x, y)

    def length(self):
        return Point.distance(self.p1, self.p2)

class Circle(object):

    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre

    def overlaps(self, other):
        if Point.distance(self.centre, other.centre) < self.radius + other.radius:
            return True
        else:
            return False

def main():
    p1 = Point(2)
    p2 = Point(6, 8)
    p3 = Point(3, 4)

    s1 = Segment(Point(), p3)
    s2 = Segment(p1, p2)
    p4 = s1.midpoint()

    c1 = Circle(p1, 5)
    c2 = Circle(p2, 2)
    c3 = Circle(p1, 2)

    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(s1.length())
    print(c1.overlaps(c2))
    print(c2.overlaps(c1))
    print(c1.overlaps(c3))
    print(c3.overlaps(c1))
    print(c3.overlaps(c2))

if __name__ == '__main__':
    main()
