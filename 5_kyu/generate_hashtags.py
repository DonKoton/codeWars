# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    if s != '' and len(s) <= 140:
        s = s.strip()
        s = [word.strip().capitalize() for word in s.split()]
        return '#' + ''.join(s)
    else:
        return False


print(generate_hashtag('codewars  is  nice'))