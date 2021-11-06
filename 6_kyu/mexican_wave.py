# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

def wave(people):
    words = [people.lower() for _ in range(len(people))]
    result = []
    for index, word in enumerate(words):
        word_list = list(word)
        if word_list[index].isalpha():
            word_list[index] = word_list[index].upper()
            result.append(''.join(word_list))
        else:
            continue
    return result


print(wave('Codewars'))
print(wave('this is mexican wave'))