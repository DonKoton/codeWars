# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python


def dirReduc(arr):
    pairs = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for i in arr:
        if result and pairs[i] == result[-1]:
            result.pop()
        else:
            result.append(i)
    return result


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))