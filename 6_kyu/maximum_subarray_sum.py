# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
    maximum = 0
    local_maximum = 0
    for i in arr:
        if local_maximum > 0:
            local_maximum += i
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
        elif i > 0:
            local_maximum += i

    return maximum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))