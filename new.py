# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

def what_century(year):
    if year.endswith('00'):
        short = int(year) // 100
    else:
        short = int(year) // 100 + 1
    if short > 20 and str(short).endswith('1'):
        stndrd = 'st'
    elif short > 20 and str(short).endswith('2'):
        stndrd = 'nd'
    elif short > 20 and str(short).endswith('3'):
        stndrd = 'rd'
    else:
        stndrd = 'th'
    return str(short)+stndrd

print(what_century('1234'))
print(what_century('2001'))
print(what_century('2000'))
print(what_century('1023'))
print(what_century('2121'))
print(what_century('2222'))