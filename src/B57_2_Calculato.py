import io
import sys

_INPUT = """\
300000 536870911
"""
"""
1,2,…,N それぞれに対して、次の操作を K 回行った後の整数を求めてください。

十進法で表したときの各位の数字の和を、自身から引く。
たとえば 108 に対して 3 回の操作を行うと、
108→99→81→72 と変化します。

普通に1からNまでK回引いてみる。
同値が連続する部分だけ、算出を省いたがTLE
数値の合算速度は calc_sum_digit(数字) > sum(map(int, str(数字)))
TLE
メモ化再帰的な実装に変更
"""
sys.stdin = io.StringIO(_INPUT)

from functools import lru_cache


@lru_cache(maxsize=1000000)
def calc_sum_digit(n):
    sumDigit = 0
    tmp = n
    while tmp > 0:
        tmp, mod = divmod(tmp, 10)
        sumDigit += mod
    return sumDigit


@lru_cache(maxsize=1000000)
def calc_minus_all_digit(a, k):
    for j in range(k):
        a -= calc_sum_digit(a)
    return a


n, k = map(int, input().split())

ans = [None] * n
# 大きい方から算出する
for i in reversed(range(1, n + 1)):
    a = i
    a -= calc_sum_digit(a)
    if k > 1:
        a = calc_minus_all_digit(a, k - 1)
    #print(i)
    ans[i - 1] = a

#print(ans)
for a in ans:
    print(a)
