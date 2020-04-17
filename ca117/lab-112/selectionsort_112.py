#!/usr/bin/env python3

# selection sort: find min and swap with index 1, find 2nd min and swap with index 2, etc.
def selectionsort(a):
    # for every item in list
    for i in range(len(a)):
        # find the minimum element
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        # swap min with i
        a[i], a[min] = a[min], a[i]

import random

def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    selectionsort(A)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()
