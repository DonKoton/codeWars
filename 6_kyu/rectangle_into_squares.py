# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python

def sqInRect(lng, wdth):
    results = []
    if lng != wdth:
        while lng*wdth != sum(result**2 for result in results):
            pair = [lng, wdth]
            lesser = min(pair)
            results.append(lesser)
            if lng != lesser:
                lng = max(pair) - lesser
            else:
                wdth = max(pair) - lesser
            if lng == 0 or wdth == 0:
                break
    else:
        return None
    return results


print(sqInRect(5, 3))
print(sqInRect(5, 5))
print(sqInRect(20, 14))
print(sqInRect(37, 14))