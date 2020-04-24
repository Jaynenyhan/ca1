#!/usr/bin/env python3

import sys

# return word with highest count of consecutive vowels
def doubles(words):
    d = {}
    vowels = 'aeiou'
    for word in words:
        count = 0
        for i in range(0, len(word)):
            curr_ch = word[i]
            if i == 0:
                prev_ch = None
            else:
                prev_ch = word[i - 1]
            if i == len(word) - 1:
                next_ch = None
            else:
                next_ch = word[i + 1]
            if curr_ch in vowels and curr_ch == next_ch != prev_ch:
                count += 1
        d[word] = count
    return max(d, key=d.get)

def main():
    words = sys.stdin.read().split()
    print(doubles(words))

if __name__ == "__main__":
    main()
