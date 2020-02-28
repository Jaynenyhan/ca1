#!/usr/bin/env python3

def swap_unique_keys_values(d):
    new_d = {}
    for k, v in d.items():
        if v not in new_d:
            new_d[v] = k
        else:
            del new_d[v]
    return new_d

def main():
    my_dict = {'a': 4, 'b': 7, 'c': 10, 'd': 7}
    new_dict = swap_unique_keys_values(my_dict)
    print(new_dict)

if __name__ == '__main__':
    main()
