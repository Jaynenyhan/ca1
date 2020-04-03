#!/usr/bin/env python3

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Shape(object):

    def __init__(self, points=[]):
        self.points = points

    def sides(self):
        sidelen = []
        for i in range(1, len(self.points)):
            sidelen.append(self.points[i - 1].distance(self.points[i]))

        sidelen.append(self.points[-1].distance(self.points[0]))
        return sidelen

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):

    def area(self):
        s = self.perimeter() / 2
        a, b, c = self.sides()
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Square(Shape):

    def area(self):
        a, b, c, d = self.sides()
        return a * b

def main():

    t1 = Triangle([Point(0, 0), Point(3, 4), Point(6, 0)])
    print(t1.sides())
    print(t1.perimeter())
    print(t1.area())

    t2 = Triangle([Point(0, 0), Point(4, 0), Point(4, 3)])
    print(t2.sides())
    print(t2.perimeter())
    print(t2.area())

    s1 = Square([Point(0, 0), Point(5, 0), Point(5, 5), Point(0, 5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()
