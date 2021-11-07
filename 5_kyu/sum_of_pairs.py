# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

def sum_pairs(ints, s):
    result = set()
    for int in ints:
        if s - int in result:
            return [s - int, int]
        result.add(int)


print(sum_pairs([1, 4, 8, 7, 3, 15], 8))