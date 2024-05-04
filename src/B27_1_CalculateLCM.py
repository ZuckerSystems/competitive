import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
1 1
"""
sys.stdin = io.StringIO(_INPUT)
"""
整数 
A と B の最小公倍数（ A,B 両方の倍数であるような正の整数 
x のうち最小のもの）を出力してください。
A Bを素因数分解する。
Aの因数がBの因数に含まれていたらB側を削除する
"""

A, B = map(int, input().split())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


aPrime = prime_factorize(A)
bPrime = prime_factorize(B)

import bisect

if len(aPrime) == 0 or len(bPrime) == 0:
    print(A * B)
else:
    ans = 1
    for a in aPrime:
        idx = bisect.bisect_left(bPrime, a)
        if idx < len(bPrime):
            if bPrime[idx] == a:
                bPrime.pop(idx)
        ans *= a
    #print(bPrime)
    for b in bPrime:
        ans *= b
    print(ans)
