import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
10
7
0 3
2 4
1 3
0 3
5 6
5 6
5 6
"""
"""
あるコンビニは時刻0 に開店し、時刻 T に閉店します。このコンビニには N 人の従業員が働いており、i 番目 (1≤i≤N) の従業員は時刻Liに出勤し、時刻Riに退勤します。
t=0,1,2,…,T-1 それぞれについて、時刻 t+0.5 にコンビニにいる従業員の数を出力するプログラムを作成してください。
0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
+   +   *   -   -   -   -
結果:AC numpyの要素代入が遅いのでちょっと改善要
"""
sys.stdin = io.StringIO(_INtdUT)
import numpy as np

t = int(input())
n = int(input())

# 1インデックスで出入り表を作成 中間の時間を取るために*2の位置に書き込み
workInOut = np.zeros(t * 2 + 1, dtype=int)

for i in range(n):

    l, r = map(int, input().split())
    workInOut[l * 2] += 1
    workInOut[r * 2] -= 1

# 出入り表から累積和を取って解答するのみ
workSum = np.cumsum(workInOut)
for i in range(1, t + 1):
    print(workSum[i * 2 - 1])
