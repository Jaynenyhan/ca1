#!/usr/bin/env python3

from math import sqrt
from stack_092 import Stack

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def negate(x):
    return -x

binops = {'+': add, '-': subtract, '*': multiply, '/': divide}
uniops = {'n': negate, 'r': sqrt}

def calculator(line):
    stack = Stack()
    for e in line.split():
        if e in binops.keys():
            y = stack.pop()
            x = stack.pop()
            stack.push(binops[e](x, y))
        elif e in uniops.keys():
            stack.push(uniops[e](stack.pop()))
        else:
            stack.push(float(e))
    return stack.top()

import sys

def main():

    for line in sys.stdin:
        try:
            a = calculator(line.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()
