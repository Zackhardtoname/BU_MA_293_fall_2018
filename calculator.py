import operator as op
from functools import reduce
from math import factorial

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

def nPr(n, r):
    return int(factorial(n)/factorial(n-r))

print(nPr(20, 20)/(nPr(4, 4))**5)


sum = 0
# for m in range(0, 11):
#     sum += ncr(10, m)
# print(sum)

# for n in range (1, 5):
#     for k in range(1, 5):
#         print(n, k, ncr(n+k-1, k-1))
#