#!/usr/bin/env python3

def l2d(f):
    lines = f.readlines()
    keys = lines[0].split()
    values = lines[1].split()
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d
