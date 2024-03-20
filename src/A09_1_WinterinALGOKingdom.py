import io
import sys

_INPUT = """\
6 5 2
1 1 5 5
2 3 3 5
"""
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
ABCD = [ None ] * N

# 地図Ｗ✕Ｈを作成
matrix = [ [ 0 ] * (W) for i in range(H) ]
# シンプルに横方向に１行毎に走査
for i in range(N):  #10000回ループするらしいのでNGだろう 10000✕1000✕1000
  A, B, C, D = map(int, input().split())
  for h in range(A - 1, C):
    for w in range(B - 1, D):
      matrix[h][w] += 1 

for h in range(H):
  print(' '.join(map(str, matrix[h])))