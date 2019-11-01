#!/usr/bin/env python

if __name__ == "__main__":
   a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
while i < len(a) and a[i] == "":
   i = i + 1

print a[i]
