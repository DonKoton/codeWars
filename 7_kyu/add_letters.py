# https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

from string import ascii_lowercase

def add_letters(*letters):
    list_of_letters = [letter for letter in letters]
    if len(list_of_letters) > 0:
        pairs = {letter: ord(letter) % 32 for letter in ascii_lowercase}
        reversed_pairs = {value: key for key, value in pairs.items()}
        sum1 = 0
        for letter in list_of_letters:
            sum1 += pairs[letter]
        if sum1 % 26 != 0:
            return reversed_pairs[sum1 % 26]
        else:
            return 'z'
    else:
        return 'z'


print(add_letters('y', 'c', 'b'))
print(add_letters('a', 'b', 'c'))
print(add_letters())
print(add_letters('t'))