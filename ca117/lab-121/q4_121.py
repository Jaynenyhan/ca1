#!/usr/bin/env python3

import sys

# convert camelcase to space separated words
def convert(s):
    chars = [ch for ch in s]
    # add first letter regardless
    out = [chars[0]]
    # for every letter except the first
    for ch in chars[1:]:
        # if its uppercase, first add a space, then add the letter in lowercase
        if ch.isupper():
            out.append(" ")
            out.append(ch.lower())
        # else just add the letter
        else:
            out.append(ch)
    # join list of chars to make string
    return "".join(out)

def main():
    for line in sys.stdin:
        s = line.strip()
        print(convert(s))

if __name__ == "__main__":
    main()
