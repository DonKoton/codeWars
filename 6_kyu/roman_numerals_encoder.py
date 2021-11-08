def solution(n):
    pairs = {1: 'I',
             2: 'II',
             3: 'III',
             4: 'IV',
             5: 'V',
             6: 'VI',
             7: 'VII',
             8: 'VIII',
             9: 'IX',
             10: 'X',
             20: 'XX',
             30: 'XXX',
             40: 'XL',
             50: 'L',
             60: 'LX',
             70: 'LXX',
             80: 'LXXX',
             90: 'XC',
             100: 'C',
             200: 'CC',
             300: 'CCC',
             400: 'CD',
             500: 'D',
             600: 'DC',
             700: 'DCC',
             800: 'DCCC',
             900: 'CM',
             1000: 'M',
             2000: 'MM',
             3000: 'MMM'}

    num = str(n)
    numbers = [digit.ljust(index, '0') for index, digit in enumerate(num[::-1], start=1)]
    numbers = [int(number) for number in numbers if not number.startswith('0')]
    result = ''.join([pairs[element][::-1] for element in numbers])
    return result[::-1]


print(solution(1889))
print(solution(14))
print(solution(91))
print(solution(45))
print(solution(112))
print(solution(997))


# alternate version

def solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'}

    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution(1889))
