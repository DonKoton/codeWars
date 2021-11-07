# https://www.codewars.com/kata/55eea63119278d571d00006a/train/python

def next_id(arr):
    arr.sort()
    if 0 not in arr:
        return 0
    else:
        for previous, current in zip(arr, arr[1:]):
            if current > previous + 1:
                return previous + 1
        return max(arr) + 1

print(next_id([0,1,2,3,4,5,6,7,8,9,10]))
print(next_id([5,4,3,2,1]))
print(next_id([0,1,2,3,5]))
print(next_id([0,0,0,0,0,0]))
print(next_id([]))
print(next_id([0,0,1,1,2,2]))
print(next_id([0,1,1,1,3,2]))
print(next_id([0,1,0,2,0,3]))
print(next_id([9,8,0,1,7,6]))
print(next_id([9,8,7,6,5,4]))
