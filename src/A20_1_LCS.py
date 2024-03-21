import io
import sys

_INPUT = """\
tokyo
kyoto
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# LCS
# 動的計画法(DP)
S = input()
T = input()

len_s = len(S)
len_t = len(T)
# DPの初期化
dp = [[0 for j in range(len_t + 1)] for i in range(len_s + 1)]

for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        # print(S[i - 1] + ':' + T[j - 1])
        if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len_s][len_t])