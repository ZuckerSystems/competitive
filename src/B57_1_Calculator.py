import io
import sys

_INPUT = """\
10 1
"""
"""
1,2,…,N それぞれに対して、次の操作を K 回行った後の整数を求めてください。

十進法で表したときの各位の数字の和を、自身から引く。
たとえば 108 に対して 3 回の操作を行うと、
108→99→81→72 と変化します。

普通にN回引いてみる
"""
sys.stdin = io.StringIO(_INPUT)


def calc_sum_digit(n):
    sumDigit = 0
    tmp = n
    while tmp > 0:
        tmp, mod = divmod(tmp, 10)
        sumDigit += mod
    return sumDigit


n, k = map(int, input().split())
pre1 = 0
preAns = 0
for i in range(1, n + 1):
    ans = i
    for j in range(k):
        #ans -= sum(map(int, str(ans)))
        ans -= calc_sum_digit(ans)
        if j == 1:
            if pre1 == ans:
                ans = preAns
                break
            pre1 = ans

        #print(i, ans)

    print(ans)
    preAns = ans
