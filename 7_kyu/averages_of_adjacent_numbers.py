# https://www.codewars.com/kata/57d2807295497e652b000139/train/python

def averages(arr):
    if not arr is None:
        return [(num1+num2)/2 for num1, num2 in zip(arr, arr[1:])]
    else:
        return []
print(averages([1, 3, 5, 1, -10]))