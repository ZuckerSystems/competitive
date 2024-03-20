
import io
import sys

_INPUT = """\
8
5
2 3
3 6
5 7
3 7
1 5
"""
sys.stdin = io.StringIO(_INPUT)

#### ここからが提出するプログラム
D = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for men in range(0, N):
  L[men], R[men] = list(map(int,input().split()))

result = [ None ] * (D + 1)

for day in range(1, D + 1):
  #print(day)
  result[day] = 0
  #print(str(day) + '日目')

  for men in range(N):
    if L[men] <= day and R[men] >= day:
      #print(str(men) + '人目参加')
      result[day] = result[day] + 1

  print(result[day])
  
