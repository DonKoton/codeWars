# https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python

def partlist(arr):
    counter = 1
    result = []
    for _ in range(len(arr)):
        string1 = ' '.join([word for word in arr[:counter]])
        string2 = ' '.join([word for word in arr[counter:]])
        result.append((string1, string2))
        counter += 1
    return result[:-1]

print(partlist(["I", "wish", "I", "hadn't", "come"]))