import io
import sys

_INPUT = """\
6
30
10
30
20
10
30
"""
"""

"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
import numpy as np

N = int(input())
A = [int(input()) for i in range(N)]

a = np.array(A)
u, counts = np.unique(a, return_counts=True)

ans = 0
for c in counts[counts > 1]:
    # 組み合わせの数のため1から出現数-1までの和 4の場合 1+2+3
    ans += (c - 1) * c // 2
print(ans)
