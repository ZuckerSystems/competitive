import io
import sys

_INPUT = """\
10 285
29 8000
43 11000
47 10000
51 13000
52 16000
66 14000
72 25000
79 18000
82 23000
86 27000
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# ナップザック問題というやつ
# こちらも動的計画法(DP)
N, W = map(int, input().split())
w = [ None ] * N
v = [ None ] * N
for i in range(N):
  w[i], v[i] = map(int, input().split())

# 横軸重さで表を作成.値に価値を入れる
dp = [[0 for j in range(W + 1)] for i in range(N)]
ans = 0

# １品目の処理 
for j in range(W + 1):
  if ｗ[0] <= j:
    dp[0][j] = v[0] # 重さが収まる範囲に価値を入れる
#print(dp)

# 商品分価値を入れる
for i in range(1, N):
  for j in range(W + 1):
    not_choice = dp[i-1][j]
    if w[i] > j:
      dp[i][j] = not_choice
    else:
      # 前の重さの位置の価値+今商品の価値を求める dp表の元位置の算出は要注意
      choice =  dp[i-1][j - w[i]] + v[i]
      dp[i][j] = max(choice, not_choice)

#for i in range(N):
#  print(dp[i])
print(dp[N -1][W])