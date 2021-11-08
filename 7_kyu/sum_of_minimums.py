# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python

def sum_of_minimums(numbers):
    return sum(map(min, numbers))

print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))