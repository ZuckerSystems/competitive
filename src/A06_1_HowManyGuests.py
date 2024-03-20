import io
import sys

_INPUT = """\
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10
"""
sys.stdin = io.StringIO(_INPUT)

NQ = list(map(int,input().split()))
N = NQ[0]
Q = NQ[1]
A = list(map(int,input().split()))
#print(AN)
L = [ None ] * Q
R = [ None ] * Q

# 合計の最大から最小の一つ前を減算する
def sum_x_to_y(num_list, x, y):
  return num_list[y] - num_list[x - 1]

for i in range(Q):
  L[i], R[i] = map(int,input().split())
  
# Qまでの加算した値をすべて保持
sumQ = [ None ] * (N + 1)
sumQ[0] = 0
for i in range(N):
  sumQ[i + 1] = sumQ[i] + A[i]


