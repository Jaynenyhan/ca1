#!/usr/bin/env python3

import sys

def floodfill(world, x, y):
    width = len(world)
    height = len(world[0])
    # if current ch isnt a star, return
    if world[x][y] != "-":
        return
    # change current ch
    world[x][y] = "."
    # recursive calls on floodfill
    if x > 0:  # go left
        floodfill(world, x - 1, y)
    if y > 0:  # go up
        floodfill(world, x, y - 1)
    if x < width - 1:  # go right
        floodfill(world, x + 1, y)
    if y < height - 1:  # go down
        floodfill(world, x, y + 1)

def lines2world(lines, width, height):
    world = []
    # create list of lists, as we need mutability
    # each list refers to a column x
    # each list contains the chars on row y of every column x
    # we do this so its easy to understand as world[x][y]
    for i in range(width):
        world.append([''] * height)
    for y in range(height):
        for x in range(width):
            world[x][y] = lines[y][x]
    return world

def stars(lines):
    # init variables
    width = len(lines[0])
    height = len(lines)
    world = lines2world(lines, width, height)
    # counting
    count = 0
    for x in range(width):
        for y in range(height):
            # when we find a star, floodfill, that will replace the rest of the star
            if world[x][y] == "-":
                floodfill(world, x, y)
                count += 1
    return count

def main():
    lines = sys.stdin.read().strip().split('\n')[1:]
    print(stars(lines))

if __name__ == '__main__':
    main()
