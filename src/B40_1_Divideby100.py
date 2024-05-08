import io
import sys

_INPUT = """\
3
100 100 100
"""
"""
2個組み合わせて100の倍数になる組み合わせを求める
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など

import numpy as np
import bisect

N = int(input())
A = list(map(int, input().split()))

npA = np.array(A) % 100

npA.sort()

a = npA.tolist()
#print(a)
ans = 0
for i in range(N):
    if a[i] > 0:
        target = 100 - a[i]
    else:
        target = 0
    targetIdx = bisect.bisect_left(a, target)
    #print(targetIdx)
    if targetIdx < N:
        #print(a[8])
        while a[targetIdx] == target:
            if i < targetIdx:
                ans += 1
            targetIdx += 1
            if targetIdx == N:
                break
print(ans)
