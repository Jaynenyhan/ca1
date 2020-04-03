#!/usr/bin/env python3

from stack_092 import Stack

def matcher(line):

    s = Stack()

    left = '({['
    right = ')}]'
    brackets = ['()', '{}', '[]']
    line = line.strip()

    try:
        for ch in line:
            if ch in left:
                s.push(ch)
            else:
                if s.top() + ch in brackets:
                    s.pop()
        return s.is_empty()
    except:
        return False

import sys

def main():

    for line in sys.stdin:
        print(matcher(line.strip()))

if __name__ == '__main__':
    main()
