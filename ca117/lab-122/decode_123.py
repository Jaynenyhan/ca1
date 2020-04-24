#!/usr/bin/env python3

import sys

# After each vowel a p is added followed by the vowel again.
def decode(s):
    vowels = 'aeiou'
    chars = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in vowels:
            chars.append(ch)
            i += 3
        else:
            chars.append(ch)
            i += 1
    return ''.join(chars)

def main():
    for line in sys.stdin:
        s = line.strip()
        print(decode(s))

if __name__ == "__main__":
    main()
