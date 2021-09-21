# https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python


def capitalize(s):
    index = 0
    string1 = ''
    string2 = ''
    for letter in s:
        if index % 2 == 0:
            string1 += letter.upper()
            string2 += letter
        else:
            string2 += letter.upper()
            string1 += letter
        index += 1
    return [string1, string2]

print(capitalize('abcdef'))

# alternative

# def capitalize(s):
#     s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
#     return [s, s.swapcase()]