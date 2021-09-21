# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = alphabet.upper()
    for num in chars:
        if num.isupper():
            li_ind2 = [alphabet2.index(num) for num in chars]
            for previous, current in zip(li_ind2, li_ind2[1:]):
                if current > previous + 1:
                    return alphabet2[current-1]
        else:
            li_ind1 = [alphabet.index(num) for num in chars]
            for previous, current in zip(li_ind1, li_ind1[1:]):
                if current > previous + 1:
                    return alphabet[current-1]


print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))