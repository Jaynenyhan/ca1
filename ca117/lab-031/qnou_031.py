#!/usr/bin/env python3

import sys

def qnou(a):
    words = [s.strip() for s in a]
    print("Words with q but no u:", [s for s in words if s.lower().count("qu") < s.lower().count("q")])

def main():
   qnou(sys.stdin.readlines())

if __name__ == '__main__':
   main()
