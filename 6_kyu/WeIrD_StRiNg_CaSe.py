# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python

def to_weird_case(string):
    indices = [index for index, letter in enumerate(string) if letter == ' ']
    string = string.split()
    new_string = ''
    for word in string:
        for index, letter in enumerate(word):
            if index % 2 == 0:
                new_string += letter.upper()
            else:
                new_string += letter
        if len(string) > 1:
            new_string += ' '
    return new_string.strip()


print(to_weird_case('This is a test'))