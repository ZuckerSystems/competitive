import io
import sys

_INPUT = """\
7
2 4 4 7 6 7
3 5 6 7 7 7
"""
sys.stdin = io.StringIO(_INPUT)

# すごろく問題
# 動的計画法
# 入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# マスの数を動的計画法で埋めながらゴールを目指す
# dp = [0 for j in range(N + 1)]
# 模範解をみてしまったが、マイナスで初期化しないと本来通らないルートの点数が最大になってしまう模様
dp = [-(10 ** 9) for j in range(N + 1)]
dp[1] = 0
pointA = 2
pointB = 3
multiple = 50
# 動的計画法
# マスに移動してきた方法が他の方法よりも高ければ採用
for i in range(1, N):
    dp[A[i - 1]] = max(dp[A[i - 1]], dp[i] + pointA)
    dp[B[i - 1]] = max(dp[B[i - 1]], dp[i] + pointB)

# 出力
# print(dp)
print(dp[N] * multiple)
