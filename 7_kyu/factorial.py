# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

def factorial(n):
    result = 1
    if 0 <= n <=12:
        for a in range(1, n+1):
            result *= a
        return result
    else:
        raise ValueError


print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(6))
print(factorial(9))
print(factorial(12))
print(factorial(15))


# alternate version

from functools import reduce


def factorial(n):
    num1 = [1, 2, 3, 4, 5]
    return reduce(lambda x, y: x*y, num1)


# alternate version 2

from itertools import accumulate
import operator


def factorial(n):
    return accumulate([1, 2, 3, 4, 5], operator.mul)

