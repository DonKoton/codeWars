# https://www.codewars.com/kata/514a6336889283a3d2000001/solutions/python

def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

print(get_even_numbers([1, 2, 4, 5, 6]))