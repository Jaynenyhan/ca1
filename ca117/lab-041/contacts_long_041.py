#!/usr/bin/env python3

import sys

def contacts(numbers, names):
    contacts_dict = {}
    with open(numbers) as f:
        numbers_list = f.readlines()
    for person in numbers_list:
        tokens = person.split()
        contacts_dict[tokens[0]] = tokens[1:]
    for name in names:
        name = name.strip()
        print('Name:', name)
        try:
            print('Phone:', contacts_dict[name][0])
            print('Email:', contacts_dict[name][1])
        except KeyError:
            print('No such contact')

def main():
    contacts(sys.argv[1], sys.stdin.readlines())

if __name__ == '__main__':
    main()
