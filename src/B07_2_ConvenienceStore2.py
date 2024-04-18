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

要素の加減算は通常のリストに対して行う。横軸をTのままとする。
あまり性能は変わらないが、
"""
sys.stdin = io.StringIO(_INtdUT)
import numpy as np

t = int(input())
n = int(input())

# 1インデックスで出入り表を作成 中間の時間を取るために*2の位置に書き込み
workInOut = [0 for _ in range(t + 1)]

for i in range(n):

    l, r = map(int, input().split())
    workInOut[l] += 1
    workInOut[r] -= 1

# 出入り表から累積和を取って解答するのみ
tmp = np.array(workInOut)
workSum = np.cumsum(workInOut)
for i in range(t):
    print(workSum[i])
