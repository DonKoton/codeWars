# https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python

def sum_triangular_numbers(n):
    if n > 0:
        results = [1]
        suma = 1
        counter = 2
        for _ in range(n-1):
            suma += counter
            counter += 1
            results.append(suma)
        return sum(results)
    return 0


print(sum_triangular_numbers(5))