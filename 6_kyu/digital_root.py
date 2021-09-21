# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(digit):
    while digit > 9:
        result = 0
        for number in str(digit):
            result += int(number)
        digit = result
    return digit

print(digital_root(1231231))
print(digital_root(65123413))
print(digital_root(61323))
print(digital_root(65857))
print(digital_root(75673456352))