# https://www.codewars.com/kata/559a28007caad2ac4e000083/solutions/python

def fibonacci(n):
    result = [1]
    for i in range(n-1):
        result.append(sum(result[-2:]))
    return result

print(fibonacci(6))

def perimeter(n):
    return 4 * sum(fibonacci(n+1))

print(perimeter(6))