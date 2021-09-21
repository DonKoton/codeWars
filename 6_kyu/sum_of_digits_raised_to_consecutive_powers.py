# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def sum_dig_pow(a, b):
    lista = []
    for num in range(a, b+1):
        suma = 0
        power = 1
        for x in str(num):
            suma += int(x)**power
            power += 1
            if num == suma:
                lista.append(suma)
    return lista


print(sum_dig_pow(1,150))
print(sum_dig_pow(1,592))
print(sum_dig_pow(70,89))
print(sum_dig_pow(90,134))
print(sum_dig_pow(134,135))