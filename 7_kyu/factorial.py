# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

def factorial(n):
    result = 1
    if 0 <= n <=12:
        for a in range(1, n+1):
            result *= a
        return result
    else:
        raise ValueError

print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(6))
print(factorial(9))
print(factorial(12))
print(factorial(15))