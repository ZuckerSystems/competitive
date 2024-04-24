import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
4 7
3 13
3 17
5 29
1 10
"""
"""
宝箱には N 個の品物が入っており、それぞれ 1 から N までの番号が付けられています。品物 i の重さは wi であり、価値は vi です。
太郎君は、いくつかの品物を選んで持ち帰りたいと考えています。
しかし、彼のナップザックには容量制限があるので、重さの合計が W 以下になるようにする必要があります。
価値の合計としてあり得る最大の値はいくつですか。

ナップザック問題
普通に解く

価値を横軸にして最小の重さをDP表にする。
DP表の値のmaxを取る

初期化の値を10**10でもうまくいかず、模範解答を見てしまった。こんな大きい値つかっていいのか
"""

sys.stdin = io.StringIO(_INtdUT)

import bisect

n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
vMax = sum(x[1] for x in wv)
INF = 1 << 60
dp = [INF] * (vMax + 1)
dp[0] = 0

for wait, value in wv:
    preDp = dp[:]
    for j in range(1, vMax + 1):
        preIndex = 0 if j - value < 0 else j - value
        preDp[j] = min(dp[j], dp[preIndex] + wait)
    dp = preDp

print(bisect.bisect_right(dp, w) - 1)
