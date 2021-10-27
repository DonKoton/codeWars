# https://www.codewars.com/kata/529b418d533b76924600085d/train/python

def to_underscore(s):
    if isinstance(s, str):
        list_of_letters = [letter for letter in s]
        list_of_idx = []
        for index, letter in enumerate(list_of_letters):
            if letter.isupper():
                list_of_idx.append(index)
        list_of_idx.sort(reverse=True)
        for idx in list_of_idx:
            list_of_letters.insert(idx, '_')
        new_string = ''.join(list_of_letters)
        new_string = new_string.lstrip('_').lower()
        return new_string
    else:
        return str(s)

print(to_underscore('TestController'))
print(to_underscore('PascalCaseString'))
print(to_underscore(94547))