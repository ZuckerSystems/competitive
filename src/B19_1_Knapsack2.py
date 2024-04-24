import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
3 100
55 2
75 3
40 2
"""
"""
宝箱には N 個の品物が入っており、それぞれ 1 から N までの番号が付けられています。品物 i の重さは wi であり、価値は vi です。
太郎君は、いくつかの品物を選んで持ち帰りたいと考えています。
しかし、彼のナップザックには容量制限があるので、重さの合計が W 以下になるようにする必要があります。
価値の合計としてあり得る最大の値はいくつですか。

ナップザック問題
普通に解く

TLE
1≤W≤10^9 だとさ
"""

sys.stdin = io.StringIO(_INtdUT)

n, w = map(int, input().split())
wait = [0] * (n + 1)
value = [0] * (n + 1)
for i in range(1, n + 1):
    wait[i], value[i] = map(int, input().split())

dp = [[0 for j in range(w + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, w + 1):
        if wait[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            #作れる価値
            #print('i', i, '重さ', j, '重さ', wait[i], '価値', value[i])
            tmp = dp[i - 1][j - wait[i]] + value[i]
            dp[i][j] = max(dp[i - 1][j], tmp)

print(dp[n][w])
