# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:41:56 2024

@author: Jacob

QuickSort Algorithm
"""

from random import randrange

def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        minimum = [i for i in array if i <= pivot]
        maximum = [i for i in array if i > pivot]
        print(f"{maximum} + {pivot} + {minimum}")
        return qsort(minimum) + [pivot] + qsort(maximum)

if __name__ == '__main__':
    array1 = [1, 5, 12, 0, -5, 66]
    print(array1)
    print(qsort(array1))
    array2 = list(range(20))
    print(array2)
    print(qsort(array2))