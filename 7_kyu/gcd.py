# https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/train/python

def mygcd(x, y):
    if(y == 0):
        return x
    else:
        return mygcd(y, x % y)

print(mygcd(30,12))