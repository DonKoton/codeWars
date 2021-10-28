# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

import re


urls = """http://google.com
http://google.co.jp
www.xakep.ru
https://youtube.com"""

def domain_name(url):
    pattern = re.compile(r"(https?|www.)?(://)?(www.)?(\w*-?\w*)\.(\w*).*")

    matches = pattern.finditer(url)

    for match in matches:
        return match.group(4)