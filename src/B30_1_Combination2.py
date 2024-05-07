import io
import sys

_INPUT = """\
84994 61497
"""
sys.stdin = io.StringIO(_INPUT)
"""
縦 H 行・横 W 列のマス目があります。上から i 行目・左から j 列目のマスを 
(i,j) とするとき、マス(1,1) から出発し、右方向か下方向の移動を繰り返して、
マス (H,W) まで行く方法は何通りありますか。
"""
# 入力
H, W = map(int, input().split())

if H == 1 and W == 1:
    print(1)
    exit(0)

import numpy as np

CONST_DIVISION = 10**9 + 7

np.set_printoptions(threshold=4800)

dp = np.zeros((H, W), dtype=np.int64)

for i in range(1, W):
    dp[0][i] = 1

for i in range(1, H):
    dp[i][0] = 1

for h in range(1, H):
    for w in range(1, W):
        #print(dp[h - 1][w])
        dp[h][w] = (dp[h - 1][w] + dp[h][w - 1]) % CONST_DIVISION

#print(dp)
print(dp[H - 1][W - 1])
