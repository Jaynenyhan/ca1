#!/usr/bin/env python3

car = r'\b\d{2}[12]\s(?:C|CE|CN|CW|D|DL|G|KE|KK|KY|L|LD|LH|LM|LS|MH|MN|MO|OY|RN|SO|T|W|WH|WX|WW)\s[1-9]\d{0,5}\b'
# \b - word boundary
# \d{2}[12] - 2 numbers, then a 1 or a 2
# \s - whitespace
# (?:C|CE|CN|CW|D|DL|G|KE|KK|KY|L|LD|LH|LM|LS|MH|MN|MO|OY|RN|SO|T|W|WH|WX|WW) - counties
# \s - another whitespace
# [1-9]\d{0,5} - number from 1-9 then between 0 and 5 other numbers (since 0, optional)
# \b - another word boundary

from re import findall
import sys

def main():

    # Verify regular expression is not overly long
    assert(len(car) < 120)

    s = sys.stdin.read()

    carlist = findall(car, s)
    print('Cars: {}'.format(carlist))

if __name__ == '__main__':
    main()
