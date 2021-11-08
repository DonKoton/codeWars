# https://www.codewars.com/kata/539de388a540db7fec000642/train/python

from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    return entered_code == correct_code and datetime.strptime(current_date, '%B %d, %Y') <= datetime.strptime(expiration_date, '%B %d, %Y')

print(check_coupon('123','123','September 5, 2014','October 1, 2014'))
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'))i