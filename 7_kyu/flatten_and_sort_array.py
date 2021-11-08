# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python

from itertools import chain

def flatten_and_sort(array):
    return sorted(list(chain(*array)))

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))