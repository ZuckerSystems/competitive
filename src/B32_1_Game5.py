import io
import sys

_INPUT = """\
20 3
6 1 3
"""
"""
N 個の石が積まれた山があり、プレイヤー 2 人が交互に石を取り合います。
各プレイヤーが 1 回のターンで取る石の数は、a1,a2,…,ak個のいずれかでなければなりません。
先に石を取り除けなくなった方が負けとするとき、先手と後手どちらが勝ちますか。


"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (N + 1)

for i in range(N):
    #print(dp)
    for a in A:
        if dp[i] == False and i + a <= N:
            dp[i + a] = True

if dp[N]:
    print('First')
else:
    print('Second')
