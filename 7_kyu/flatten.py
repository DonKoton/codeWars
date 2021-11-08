# https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python
# flatten with different types of data when unpacking isn't necessary

from itertools import chain


def flatten(lst):
    try:
        return list(chain(*lst))
    except TypeError:
        return list(chain(lst))


print(flatten([1,2,3]))
print(flatten([[1,2,3],["a","b","c"],[1,2,3]]))