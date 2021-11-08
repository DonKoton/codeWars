# https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e/train/python

def max_number(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

print(max_number(213))