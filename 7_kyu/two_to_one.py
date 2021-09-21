# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
    long = a1 + a2
    lista = list(set([letter for letter in long]))
    lista.sort()
    return ''.join(lista)