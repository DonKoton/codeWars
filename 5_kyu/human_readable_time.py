# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    hh = seconds // 3600
    mm = int((seconds / 3600 - hh) * 60)
    ss = seconds % 60
    hh = f'{hh:02d}'
    mm = f'{mm:02d}'
    ss = f'{ss:02d}'
    return f'{hh}:{mm}:{ss}'

print(make_readable(312313))
print(make_readable(5123))
print(make_readable(123123))
print(make_readable(6454))
print(make_readable(67))
print(make_readable(60))
print(make_readable(3600))