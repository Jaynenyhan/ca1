#!/usr/bin/env python3

import sys

def rps(p1, p2):
    # draw
    if p1 == p2:
        return 'Draw'
    # rock outcomes
    if p1 == 'rock':
        if p2 == 'scissors':
            return 'Player 1 wins'
        else:
            return 'Player 2 wins'    
    # paper outcomes
    if p1 == 'paper':
        if p2 == 'rock':
            return 'Player 1 wins'
        else:
            return 'Player 2 wins'    
    # scissors outcomes
    if p1 == 'scissors':
        if p2 == 'paper':
            return 'Player 1 wins'
        else:
            return 'Player 2 wins'

def main():
    for line in sys.stdin:
        p1, p2 = line.split()
        print (rps(p1, p2))

if __name__ == "__main__":
    main()
