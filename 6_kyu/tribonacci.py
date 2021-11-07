#    https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    index = 0
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n > 2:
        for number in range(n-3):
            suma = 0
            suma += signature[index] + signature[index+1] + signature[index+2]
            signature.append(suma)
            index += 1
            if index == n-3:
                break
    return signature


# alternate version

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3):
      res.append(sum(res[-3:]))
  return res
