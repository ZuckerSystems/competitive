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
P = [None] * (N + 1)
A = [None] * (N + 1)
for i in range(1, N+1):
    P[i], A[i] = map(int, input().split())
