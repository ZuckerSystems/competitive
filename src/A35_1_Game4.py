
import io
import sys

_INPUT = """\
4
20 10 30 40
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A = list(map(int, input().split()))
# 2≤N≤2000
# 1≤Ai≤100000

# 貰うDPで最終列までDP表を作成する
dp = [[0 for j in range(N + 2)] for i in range(N)]

# 手番を決定するための変数
turn = N - 1 % 2

for i in range(N):
    if i == 0:
        for j in range(0, N):
            dp[i][j+1] = A[j]

        # print(i, dp[i])

    else:
        for j in range(1, N):
            # print(i, j, N, dp[i-1][j], dp[i-1][j+1])

            # DP表を作るi行目の手番は実際の手番の逆の人がDP表を作っておくイメージ
            if (i + turn) % 2 == 0:  # 大きい方
                # print('big')
                dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
            else:  # 小さい方
                # print('small')
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])

            if N - j == 1:
                # print('break')
                break
        # print(i, dp[i])
# print(N-2)
print(dp[N-1][1])
