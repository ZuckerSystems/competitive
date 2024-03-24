from sympy import primerange
def fact2fct(n):   # nの階乗の素因数分解
  ret = dict()
  for p in primerange(2,n+1):
    ret[p], pp = 0, p
    while pp <= n:
      ret[p] += n // pp
      pp *= p
  return ret

N = 10
print(N, fact2fct(N))