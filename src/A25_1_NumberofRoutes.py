import io
import sys

_INPUT = """\
4 8
.....#..
........
..#...#.
#.......
"""
sys.stdin = io.StringIO(_INPUT)

# ここから提出
# DP
# 入力
H, W = map(int, input().split())
C = [None] * H
for i in range(H):
    C[i] = list(input())
    #print(C[i])

dp = [([0] * (W)) for j in range(H)]

dp[0][0] = 1 # ここは#ではない
# 1行目
for h in range(1, H):
    if C[h][0] == '#':
        break
    else:
        dp[h][0] = 1
# 1列目
for w in range(1, W):
    if C[0][w] == '#':
        break
    else:
        dp[0][w] = 1
# 2行2列目からループ
for h in range(1, H):
    for w in range(1, W):
        # '#'はそのまま'.'は左と上を加算
        if C[h][w] != '#':
            dp[h][w] = dp[h-1][w] + dp[h][w -1]

#print(*dp, sep='\n')

print(dp[H -1][W -1])