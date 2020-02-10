#!/usr/bin/env python3

import sys

def beststudent(filename):
    total = 0
    try:
        with open(filename) as f:
            for data in f:
                data = data.split()
                try:
                    if int(data[0]) > total:
                        total = int(data[0])
                        name = " ".join((data[1:]))
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(data[0]))
        print('Best student:', name)
        print('Best mark:', total)
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))

def main():
    filename = sys.argv[1]
    beststudent(filename)

if __name__ == '__main__':
    main()
