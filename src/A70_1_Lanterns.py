import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
4 2
0 1 1 0
1 2 3
2 3 4
"""
sys.stdin = io.StringIO(_INPUT)

INF = 1 << 60
#print(INF)
n, m = map(int, input().split())
a = int(input()[::-1].replace(" ", ""), 2)
dp = [INF] * (1 << n)
dp[a] = 0
for i in range(m):
    x, y, z = map(int, input().split())
    num = ((1 << x) + (1 << y) + (1 << z)) >> 1
    ndp = [INF] * (1 << n)
    for j in range(1 << n):
        ndp[j] = min(ndp[j], dp[j])
        ndp[j ^ num] = min(ndp[j ^ num], dp[j] + 1)
    dp = ndp
if dp[-1] >= INF:
    print(-1)
else:
    print(dp[-1])
