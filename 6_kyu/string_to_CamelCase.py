# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    text2 = ''
    if text != '':
        for char in text:
            if char.isalpha():
                text2 += char
            else:
                char = ' '
                text2 += char
        lista = [word for word in text2.split()]
        new = f'{lista[0]}'
        for sth in lista[1:]:
            sth = sth.capitalize()
            new += sth
        return new
    else:
        return ''

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))