# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25/train/python

def vert_mirror(strng):
    return '\n'.join([el[::-1] for el in strng.split()])
def hor_mirror(strng):
    return '\n'.join(strng.split()[::-1])
def oper(fct, s):
    return fct(s)

print(hor_mirror("lVHt\nJVhv\nCSbg\nyeCt"))
print(vert_mirror("lVHt\nJVhv\nCSbg\nyeCt"))
print()
print(oper(vert_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))
print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))