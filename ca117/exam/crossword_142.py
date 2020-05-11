#!/usr/bin/env python3

import sys

def crossword(word_a, word_b):
    world = generate_world(word_a, word_b)
    pos_a, pos_b = common_char(word_a, word_b)
    # put word a in correct pos
    for i in range(0, len(word_a)):
        world[pos_b][i] = word_a[i]
    # put word b in correct pos
    for i in range(0, len(word_b)):
        world[i][pos_a] = word_b[i]
    # prepare world for printing
    lines = [''.join(line) for line in world]
    return '\n'.join(lines)

# list[row][column]
def generate_world(word_a, word_b):
    world = []
    for i in range(0, len(word_b)):
        world.append(['.'] * len(word_a))
    return world

# find pos of first common char
def common_char(s, t):
    i = 0
    while s[i] not in t:
        i += 1
    j = 0
    while t[j] != s[i]:
        j += 1
    return i, j

def main():
    word_a, word_b = sys.stdin.read().split()
    print (crossword(word_a, word_b))

if __name__ == "__main__":
    main()
