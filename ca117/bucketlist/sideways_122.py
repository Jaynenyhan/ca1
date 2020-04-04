#!/usr/bin/env python3

import sys

def lines2words(lines):
    words = []
    word_count = len(lines[0])
    word_len = len(lines)
    # create blank words
    for i in range(word_count):
        words.append('')
    for i in range(word_count):
        for j in range(word_len):
            # for every jth line, add the ith letter to the ith word
            # eg add first letter to first word for each line, then second letter to second word for each line, etc.
            words[i] += lines[j][i]
    return words

def words2lines(words):
    lines = []
    word_count = len(words)
    word_len = len(words[0])
    # create blank lines
    for i in range(word_len):
        lines.append('')
    for i in range(word_len):
        for j in range(word_count):
            # for every jth word, add the ith letter to the ith line
            # eg add first ch of first word to first line, then first ch of second word to first line, etc.
            lines[i] += words[j][i]
    return lines

def main():
    words = lines2words(sys.stdin.read().split())
    # key=str.casefold to ignore case
    sorted_words = sorted(words, key=str.casefold)
    sideways = "\n".join(words2lines(sorted_words))
    print(sideways)

if __name__ == '__main__':
    main()
