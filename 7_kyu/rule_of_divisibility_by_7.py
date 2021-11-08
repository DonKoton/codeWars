# https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python

def seven(m):
    counter = 0
    while len(str(m)) > 2:
        number1 = m // 10
        number2 = 2 * (m % 10)
        m = number1 - number2
        counter += 1
    return m, counter


print(seven(1603))
print(seven(483595))
print(seven(2340029794923400297949))