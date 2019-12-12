#!/usr/bin/env python

def selection_sort(a):
   i = 0
   while i < len(a):

      smallest = i

      j = i + 1
      while j < len(a):
         if a[j] < a[smallest]:
            smallest = j
         j = j + 1

      tmp = a[i]
      a[i] = a[smallest]
      a[smallest] = tmp

      i = i + 1

   return a
