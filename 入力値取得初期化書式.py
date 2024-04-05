import io
import sys

_INPUT = """\
3
3 5 1
"""
sys.stdin = io.StringIO(_INPUT)

# 入力
N = int(input())
A = list(map(int, input().split()))
S = input()
T = input()

len_s = len(S)
len_t = len(T)
# DPの初期化包括表記
dp = [[0 for j in range(len_t + 1)] for i in range(len_s + 1)]
# リストの包括表記
route = [list() for j in range(N + 1)]
P = [None] * (N + 1)
A = [None] * (N + 1)
for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())
    N, M, B = map(int, input().split())

LRH = [[0, 0, 0] for i in range(N)]
for i in range(N):
    LRH[i] = list(map(int, input().split()))
"""
s1 t1 u1
s2 t2 u2
s3 t3 u3
...
sn tn un
"""
a = [list(map(int, input().split(" "))) for i in range(N)]

N, L = map(int, input().split())
A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = input().split()
    A[i] = int(A[i])
