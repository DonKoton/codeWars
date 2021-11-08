# https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python

def adjacent_element_product(array):
    results = []
    for num1, num2 in zip(array, array[1:]):
        results.append(num1 * num2)
    return max(results)

print(adjacent_element_product([5, 1, 2, 3, 1, 4]))
