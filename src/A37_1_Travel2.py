
import io
import sys

_INPUT = """\
2 3 100
10 20
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

sumA = sum(A)
sumC = sum(C)

print(sumA * M + sumC * N + N * M * B)
