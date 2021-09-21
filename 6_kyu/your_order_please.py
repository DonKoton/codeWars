# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    order_num = 1
    lista = []
    splitted = sentence.split()
    while len(lista) < len(splitted):
        for word in splitted:
            if str(order_num) in word:
                lista.append(word)
                order_num += 1
    return ' '.join(lista)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))