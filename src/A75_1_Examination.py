import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
5
20 70
30 70
30 50
30 100
20 60
"""
sys.stdin = io.StringIO(_INPUT)
"""
次郎君N問からなる期末試験を受けることになりました。各設問には1からNまでの番号が付けられており、設問iは連続するTi分間を使って考えると正解にたどり着けます。
しかし、各設問には締切が定められており、設問i は試験開始時刻から Di 分後を過ぎると回答できなくなります。
次郎君が最適な行動をしたとき、最大で何問正解することができるかを求めてください。
"""
# 所要時間が短く終了時間が早いが収まるものから解いていく
#import numpy as np

n = int(input())
td = [[] for i in range(n)]
for i in range(n):
    td[i] = list(map(int, input().split()))

td = sorted(td)
time = 0
count = 0
solve = True
while solve:
    solve = False
    for i in range(n):
        if time + td[i][0] <= td[i][1]:
            time += td[i][0]
            count += 1
            solve = True
            #print(i + 1)

print(count)
