# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

import string

def is_pangram(s):
    new = ''
    for char in s:
        if char.isalpha():
            new += char.lower()
    new = set(new)
    if len(new) == len(string.ascii_lowercase):
        return True
    else:
        return False


# alternative

# import string
#
# def is_pangram(s):
#     return len(string.ascii_lowercase) <= len(set(s.lower()))

print(is_pangram('The quick, brown fox jumps over the lazy dog!'))