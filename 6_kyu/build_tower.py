# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    lista = []
    sp_num = n_floors
    st_num = 1
    star = '*'
    sp = ' '
    for i in range(n_floors):
        lista.append(f'{(sp_num-1)*sp}{st_num*star}{(sp_num-1)*sp}')
        sp_num -= 1
        st_num += 2
    return lista


# alternative

# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


print(tower_builder(15))
