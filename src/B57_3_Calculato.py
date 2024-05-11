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
メモ化再帰的な実装に変更 拾ってきた正答 実力不足で意味がわかりません
数学的な解で９で割るとかやっていそう。
あらかじめ34000までの合計を計算して拾ってくるみたいね
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

memo = [[None] * 34000 for _ in range(31)]
for i in range(34000):
    n = 9 * i
    memo[0][i] = n
    while n:
        memo[0][i] -= n % 10
        n //= 10

for i in range(30):
    for j in range(34000):
        memo[i + 1][j] = memo[i][memo[i][j] // 9]

for i in range(N):
    tmp = i + 1
    tmp2 = i + 1
    while tmp2 > 0:
        tmp -= tmp2 % 10
        tmp2 //= 10
    cnt = K - 1
    n = 0
    while cnt:
        if cnt % 2:
            tmp = memo[n][tmp // 9]
        cnt //= 2
        n += 1
    print(tmp)
