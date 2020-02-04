#!/usr/bin/env python3

import sys

def token_count(a):
   print(len(a))

def main():
   token_count(sys.stdin.read().split())

if __name__ == '__main__':
   main()
