# https://www.codewars.com/kata/5274e122fc75c0943d000148/train/python

def group_by_commas(n):
    n = list(str(n))
    length = len(n)
    lista = [x for x in range(length-3,0,-3)]
    for x in lista:
        n.insert(x, ',')
    return ''.join(n)

print(group_by_commas(1000000000000000))