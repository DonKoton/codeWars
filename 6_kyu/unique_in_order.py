# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    index = 1
    lista = []
    if len(iterable) != 0:
        for char in iterable[1:]:
            if char == iterable[index-1]:
                pass
            else:
                lista.append(iterable[index-1])
            index += 1
        lista.append(iterable[-1])
    else:
        return []
    return lista

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('JJJJJWWWWAAAEPTTTPOOOQZZZQQQ'))