import io
import sys

_INPUT = """\
7 10
11 12 16 22 27 28 31
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))

# AからKまでループしながら差分を算出 K を超えたら次へ
ans = 0
R = 1

# しゃくとり法
# Lの移動範囲
for L in range(N - 1):
  # print('L=' + str(L))
  # print('R=' + str(R))

  # Rの移動範囲
  # Aは昇順にソートされている 
  # Rが右に移動すると差は小さくなる
  while R < N and (A[R] - A[L]) <= K:
    R += 1

  # Rが範囲外になったが加算は済んでいる
  # 次のRの位置までとLとの差分は全て条件を満たす
  # print('加算値=' + str(R - L -1))
  ans = ans + R - L - 1

  if R > N: break # whileの条件にも書いているんだが
  
print(ans)
