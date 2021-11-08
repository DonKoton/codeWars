# https://www.codewars.com/kata/58daa7617332e59593000006/train/python

from functools import reduce


def find_longest(arr):
    result = reduce(lambda x, y: x if len(str(x)) >= len(str(y))  else y, arr)
    return result

print(find_longest([1, 10, 100]))
print(find_longest([1, 100, 500]))