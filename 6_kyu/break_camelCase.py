# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python


def solution(s):
    list_of_letters = [letter for letter in s]
    list_of_idx = []
    for index, letter in enumerate(list_of_letters):
        if letter.isupper():
            list_of_idx.append(index)
    list_of_idx.sort(reverse=True)
    for idx in list_of_idx:
        list_of_letters.insert(idx, ' ')
    return ''.join(list_of_letters)

print(solution('breakCamelCase'))