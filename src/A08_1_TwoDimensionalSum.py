
import io
import sys

_INPUT = """\
5 5
2 0 0 5 1
1 0 3 0 0
0 8 5 0 2
4 1 0 0 6
0 9 2 7 0
2
2 2 4 5
1 1 5 5
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
X = [ None ] * H
for h in range(H):
  X[h] = list(map(int,input().split()))

Q = int(input())
ABCD = [ None ] * Q
for q in range(Q):
  ABCD[q] = list(map(int,input().split()))

#print(X)
#print(ABCD)

# 出題数分ループ
for q in range(Q):
  a = ABCD[q][0] - 1
  b = ABCD[q][1] - 1
  c = ABCD[q][2]
  d = ABCD[q][3]  

  ans = 0
  for i in range(a, c):
    for j in range (b , d):
      #print(str(i) + ',' + str(j) + ':' + str(X[i][j]))
      ans = ans + X[i][j]
  
  print(ans)
