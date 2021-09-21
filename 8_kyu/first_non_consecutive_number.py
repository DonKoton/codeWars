# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

def first_non_consecutive(arr):
    for previous, current in zip(arr, arr[1:]):
        if current > previous + 1:
            return current

print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))
print(first_non_consecutive([4,6,7,8,9,11]))
print(first_non_consecutive([4,5,6,7,8,9,11]))
print(first_non_consecutive([-5,-4,-3,-1]))