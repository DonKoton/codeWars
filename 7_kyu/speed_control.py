# https://www.codewars.com/kata/56484848ba95170a8000004d/train/python

def gps(s, x):
    if s > 0 and len(x) > 1:
        return max([(3600 * (dist2 - dist1)) / s for dist1, dist2 in zip(x, x[1:])]) // 1
    else:
        return 0


print(gps(12, [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]))
print(gps(19, [0.0, 0.2, 0.4, 0.69, 0.92, 1.15, 1.38, 1.61, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36]))