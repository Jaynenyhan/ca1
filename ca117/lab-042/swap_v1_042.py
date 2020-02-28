#!/usr/bin/env python3

def swap_keys_values(d):
    for k, v in d.items():
        d[v] = k
        del d[k]
    return d

def main():
    my_dict = {'a': 4, 'b': 7, 'c': 10}
    new_dict = swap_keys_values(my_dict)
    print(new_dict)

if __name__ == '__main__':
    main()
