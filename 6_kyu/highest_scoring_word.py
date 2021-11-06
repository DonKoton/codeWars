# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(string):
    sums = []
    string = string.split()
    for word in string:
        word = list(word)
        sum1 = 0
        for letter in word:
            sum1 += ord(letter)%32
        sums.append(sum1)
    return string[sums.index(max(sums))]


print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
print(high('man i need a taxi up to ubud'))