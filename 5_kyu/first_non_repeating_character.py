# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

from collections import Counter

def first_non_repeating_letter(string):
    if not string or 1 not in Counter(string).values():
        return ''
    string_lower = string.lower()
    for index, char in enumerate(string_lower):
        if string_lower.count(char) == 1 and list(string)[index].isupper() and char.isalpha():
            if not char.isalpha():
                continue
            else:
                return char.upper()
        elif string_lower.count(char) == 1 and list(string)[index].islower() and char.isalpha():
            if not char.isalpha():
                continue
            else:
                return char
        elif not char.isalpha() and string.count(char) == 1:
            return char

print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))
print(first_non_repeating_letter(''))
print(first_non_repeating_letter('abbabba'))


# alternate version

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""
