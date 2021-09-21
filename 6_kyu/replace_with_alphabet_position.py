# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

import string

def alphabet_position(text):
    alphabet = {letter:str(index) for index, letter in enumerate(string.ascii_lowercase, start=1)}
    numbers = ''
    for char in text.lower():
        if char.isalpha() and char in alphabet:
            numbers += alphabet.get(char) + ' '
    numbers = numbers.strip()
    return numbers


print(alphabet_position('Red tomatoes grow in 100 months'))
print(alphabet_position('The narwhal bacons at midnight.'))