import io
import sys

_INPUT = """\
869 120
"""
sys.stdin = io.StringIO(_INPUT)
"""
縦 H 行・横 W 列のマス目があります。上から i 行目・左から j 列目のマスを 
(i,j) とするとき、マス(1,1) から出発し、右方向か下方向の移動を繰り返して、
マス (H,W) まで行く方法は何通りありますか。

dpではあり得ないくらいdp表が大きくなるので
数式化して解くのが正解だが・・・プログラミングではない
お数学 フェルマーの小定理まで理解していないと
"""

MOD = 10**9 + 7
W, H = map(int, input().split())

a = 1
for i in range(1, H + W - 2 + 1):
    a *= i
    a %= MOD

b = 1
for i in range(1, H - 1 + 1):
    b *= i
    b %= MOD
for i in range(1, W - 1 + 1):
    b *= i
    b %= MOD

ans = (a * pow(b, MOD - 2, MOD)) % MOD
print(ans)
