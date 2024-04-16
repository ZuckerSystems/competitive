import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
5
5 10
5 11
4 20
8 25
10 30
"""
sys.stdin = io.StringIO(_INtdUT)
"""
次郎君N問からなる期末試験を受けることになりました。各設問には1からNまでの番号が付けられており、設問iは連続するTi分間を使って考えると正解にたどり着けます。
しかし、各設問には締切が定められており、設問i は試験開始時刻から Di 分後を過ぎると回答できなくなります。
次郎君が最適な行動をしたとき、最大で何問正解することができるかを求めてください。
"""

# 横軸に時間を取り終了時間が短い順にソートした値でDP表を更新する 時間が30の場合の例
#5 10
#5 11
#4 20
#8 25
#10 30
#  0123456789012345678901234567890
#1 0000111111000000000000000000000
#2 0000111112200000000000000000000
#3 0001111122222233111110000000000
#4 0000111112222233233333442200000
#5 0000111112222233233333444434444

import numpy as np

td = list()
n = int(input())
for i in range(n):
    td.append(tuple(map(int, input().split())))

D_MAX = 1440
dp = np.zeros((n + 1, D_MAX + 1), dtype=np.int64)
td.sort(key=lambda x: x[1])

for i in range(n):
    t, d = td[i]
    for j in range(D_MAX + 1):
        if j < t:
            dp[i + 1][j] = dp[i][j]
        elif j <= d:
            # 前の問題を解き終えた時間に1加算したものと現在値を比較する
            dp[i + 1][j] = max(dp[i][j - t] + 1, dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]
    #print(i)
    #print(dp)
print(np.amax(dp))
