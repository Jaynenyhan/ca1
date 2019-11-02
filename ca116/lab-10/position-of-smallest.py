#!/usr/bin/env python

if __name__ == "__main__":
   a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

# Get position of minimum
i = 0
minimum = i
while i < len(a):
   if a[i] < a[minimum]:
      minimum = i
   i = i + 1

print minimum
