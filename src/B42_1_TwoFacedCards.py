import io
import sys

_INPUT = """\
5
2 8
4 -5
5 -3
-4 1
-2 -3
"""
"""
[スコア]=[選んだカードにおける表の総和の絶対値]
+[選んだカードにおける裏の総和の絶対値]

簡単な問題
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など

N = int(input())
A = [None] * (N + 1)
B = [None] * (N + 1)

ans = [0, 0, 0, 0]  # AB A-B -AB -A-B の４パターンの合計の最大
for i in range(1, N + 1):
    A[i], B[i] = map(int, input().split())
    if A[i] + B[i] > 0:
        ans[0] += A[i] + B[i]
    if A[i] - B[i] > 0:
        ans[1] += A[i] - B[i]
    if -A[i] + B[i] > 0:
        ans[2] += -A[i] + B[i]
    if -A[i] - B[i] > 0:
        ans[3] += -A[i] - B[i]

print(max(ans))
