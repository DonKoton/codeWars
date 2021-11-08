# https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python

from functools import reduce

def sum_of_n(n):
    results = []
    for x in range(abs(n) + 1):
        results.append(reduce(lambda x, y: x + y, [i for i in range(x+1)]))
    if n < 0:
        results = [-x for x in results]
    return results


print(sum_of_n(3))
print(sum_of_n(-4))