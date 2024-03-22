import io
import sys

_INPUT = """\
8
8 100
7 100
6 100
5 100
4 100
3 100
2 100
1 100
"""
sys.stdin = io.StringIO(_INPUT)

# 設問の意味が不明のため例解のまま
# 入力
N = int(input())
P = [None] * (N + 1)
A = [None] * (N + 1)
for i in range(1, N+1):
    P[i], A[i] = map(int, input().split())

# 動的計画法（LEN は r-l の値)
dp = [[None] * (N + 1) for i in range(N + 1)]
dp[1][N] = 0
for LEN in reversed(range(0, N-1)):
    for l in range(1, N-LEN+1):
        r = l + LEN

        # score1 の値（l-1 番目のブロックを取り除くときの得点）を求める
        score1 = 0
        if l >= 2 and l <= P[l-1] and P[l-1] <= r:
            score1 = A[l-1]
            print(score1)

        # score2 の値（r+1 番目のブロックを取り除くときの得点）を求める
        score2 = 0
        if r <= N-1 and l <= P[r+1] and P[r+1] <= r:
            score2 = A[r+1]
            print(score2)

        # dp[l][r] を求める
        if l == 1:
            dp[l][r] = dp[l][r+1] + score2
        elif r == N:
            dp[l][r] = dp[l-1][r] + score1
        else:
            dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)
            print('MAX:' + str(dp[l][r]))

        print(dp)
        #
# 出力
Answer = 0
for i in range(1, N+1):
    Answer = max(Answer, dp[i][i])
print(Answer)
