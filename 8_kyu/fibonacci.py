def fibonacci(n):
    result = [1]
    for i in range(n - 2):
        result.append(sum(result[-2:]))
    return result

print(fibonacci(10))
