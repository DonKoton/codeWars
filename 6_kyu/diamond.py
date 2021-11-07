# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python


def diamond(n):
    lista = []
    sp_num = n
    st_num = 1
    for i in range(n//2+1):
        lista.append(f"{(sp_num-1)*' '}{st_num*'*'}")
        sp_num -= 1
        st_num += 2
    sp_num += 2
    st_num -= 4
    for i in range(n//2):
        lista.append(f"{(sp_num-1)*' '}{st_num*'*'}")
        sp_num += 1
        st_num -= 2

    return '\n'.join(lista) + '\n'


print(diamond(5))


# alternate version - cleaner


def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None
