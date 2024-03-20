import io
import sys

_INPUT = """\
3000 4000
"""
sys.stdin = io.StringIO(_INPUT)

nk = list(map(int,input().split()))
n = nk[0]
k = nk[1]

result = 0
#print(n)
#print(k)
for r1 in range(1 , n + 1):
  for r2 in range(1, n + 1):
    if r1 + r2 >= k: break
    r3 = k - r1 - r2
    # r3が条件を満たすか
    #print('r3=' + str(r3) + 'g=' + str(r1 + r2 + r3))
    if r3 >= 1 and r3 <= n:
      #print('加算')
      result += 1
print(result)