# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

def good_vs_evil(good, evil):
    good = list(map(int, good.split()))
    evil = list(map(int, evil.split()))
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    good_pts = sum([g_worth * g_units for g_worth, g_units in zip(good_worth, good)])
    evil_pts = sum([e_worth * e_units for e_worth, e_units in zip(evil_worth, evil)])
    if evil_pts > good_pts:
        return 'Battle Result: Evil eradicates all trace of Good'
    elif good_pts > evil_pts:
        return 'Battle Result: Good triumphs over Evil'
    else:
        return 'Battle Result: No victor on this battle field'


print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 0 0 0'))