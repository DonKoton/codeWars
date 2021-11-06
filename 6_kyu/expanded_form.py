# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
    num = str(num)
    numbers = [digit.ljust(index, '0') for index, digit in enumerate(num[::-1], start=1)]
    numbers = [number for number in numbers if not number.startswith('0')]
    return ' + '.join(numbers[::-1])


print(expanded_form(70304))
print(expanded_form(8912891))