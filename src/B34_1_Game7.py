import io
import sys

_INPUT = """\
2 2 3
5 8
"""
sys.stdin = io.StringIO(_INPUT)

# nim=5
GRUNDY = [0, 0, 1, 1, 2]
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

xorSum = 0
for i in range(N):
    xorSum ^= GRUNDY[A[i] % 5]
if xorSum >= 1:
    print("First")
else:
    print("Second")
