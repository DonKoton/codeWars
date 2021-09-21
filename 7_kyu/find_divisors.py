# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python

def divisors(integer):
    lista = [num for num in range(2, integer) if integer != 0 and integer % num == 0]
    if lista == []:
        return f'{integer} is prime'
    else:
        return lista

print(divisors(123123))
print(divisors(12))
print(divisors(54))
print(divisors(81))
print(divisors(12341))
print(divisors(99999))