import io
import sys

_INPUT = """\
4 11
3 1 4 5
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# こちらも動的計画法(DP)
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0 for j in range(S + 1)] for i in range(N)]
ans = 'No'
for i in range(S + 1):
  if A[0] <= i:
    dp[0][i] = A[0]
#print(dp)
for i in range(1, N):
  for j in range(S + 1):
    not_choice = dp[i-1][j]
    if A[i] > j:
      dp[i][j] = not_choice
    else:
      choice =  dp[i-1][j - A[i]] + A[i]
      dp[i][j] = max(choice, not_choice)
      if dp[i][j] == S:
        ans = 'Yes'
        break
#print(dp)
print(ans)