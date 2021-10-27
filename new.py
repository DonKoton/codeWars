arr = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
for previous, current in zip(arr, arr[1:]):
    if current > previous + 1:
        print(current)
