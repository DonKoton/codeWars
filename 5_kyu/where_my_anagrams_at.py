# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

def anagrams(word, words):
    word = ''.join(sorted(word))
    return [x for x in words if ''.join(sorted(x)) == word]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))