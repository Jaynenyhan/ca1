#!/usr/bin/env python3

import sys

def censor(s, censored_words):
    for word in censored_words:
        s = s.replace(word, "@" * len(word))
    print(s)

def main():
    with open(sys.argv[1]) as f:
        censored_words = f.read().split()
    for line in sys.stdin:
        s = line.strip()
        censor(s, censored_words)

if __name__ == '__main__':
    main()
