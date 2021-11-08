# https://www.codewars.com/kata/586909e4c66d18dd1800009b/train/python

def multiply_all(array):
    def multiply(value):
        return [i * value for i in array]

    return multiply


print(multiply_all([1, 2, 3])(2))