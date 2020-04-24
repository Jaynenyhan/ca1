#!/usr/bin/env python3

import sys
from string import punctuation

def nodups(lines):
    seen = []
    out = []
    for line in lines:
        words = line.split()
        for i in range(0, len(words)):
            word_minus_punc = ''.join([ch for ch in words[i].lower() if ch not in punctuation])
            if word_minus_punc not in seen:
                seen.append(word_minus_punc)
            else:
                words[i] = '.'
        out.append(' '.join(words))
    return '\n'.join(out)

def main():
    lines = sys.stdin.readlines()
    print(nodups(lines))

if __name__ == "__main__":
    main()
