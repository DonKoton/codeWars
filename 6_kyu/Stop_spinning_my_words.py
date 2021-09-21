# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    sentence = sentence.split()
    sentence2 = [word[::-1] if len(word) > 4 else word for word in sentence]
    return ' '.join(sentence2)


print(spin_words('Where was Gondor when the Westfold fell?'))

