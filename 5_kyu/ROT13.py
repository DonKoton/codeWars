# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

from string import ascii_lowercase


def rot13(message):
    doubled_alphabet = list(ascii_lowercase*2)
    indices = [doubled_alphabet.index(letter) if letter.isalpha() else letter for letter in message.lower()]
    rot13_message = []
    for index in indices:
        if isinstance(index, int):
            rot13_message.append(doubled_alphabet[index+13])
        else:
            rot13_message.append(index)
    upper_indices = [index for index, letter in enumerate(message) if letter.isupper()]
    for index in upper_indices:
        rot13_message[index] = rot13_message[index].upper()
    return ''.join(rot13_message)

print(rot13('izyHdHVtqbNKTkh0'))
print(rot13('what time are we climbing up the volcano'))