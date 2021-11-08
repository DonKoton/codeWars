# https://www.codewars.com/kata/534d0a229345375d520006a0/train/python

def power_of_two(x):
    counter = 0
    result = []
    while True:
        result.append(2**counter)
        counter += 1
        if x in result:
            return True
        elif result[-1] > x:
            return False

print(power_of_two(4096))
print(power_of_two(333))
