
import io
import sys

_INPUT = """\
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# 
# 動的計画法(DP)で算出する。
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ 0 ] * (N + 1)
dp[1] = 0
dp[2] = A[0] # 2部屋目に到着するのはA側のみ
aroute = 0
broute = 0
# 3部屋目以降に到着するのがAルートかBルートか早いのを算出する
for i in range(3, N + 1):
	aroute = dp[i - 1] + A[i - 2]
	broute = dp[i - 2] + B[i - 3]
	dp[i] = min(aroute, broute)

#print(dp)
print(dp[N])

