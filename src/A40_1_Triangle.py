import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
7
1 2 1 2 1 2 1
"""
sys.stdin = io.StringIO(_INPUT)

# 同じ長さの棒をカウントする
N = int(input())
A = [0] * N
A = list(map(int, input().split()))

import collections

c = collections.Counter(A)

ans = 0
for l in c.values():
    if l >= 3:
        #print(l)
        # nPr / r!
        rf = 6
        nPr = l * (l - 1) * (l - 2)
        ans += int(nPr / rf)

print(ans)
