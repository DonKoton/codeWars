# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
# drop duplicates from list keeping the elements order

def distinct(seq):
    result = []
    for a in seq:
        if a not in result:
            result.append(a)
    return result


# alternatywa

# def distinct(seq):
#     return sorted(set(seq), key = seq.index)

print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))
print(distinct([2, 5, 7, 2, 3, 8, 1, 4, 5, 7, 9, 7, 0, 2]))