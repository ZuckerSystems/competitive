
import io
import sys

_INPUT = """\
2 2 3
5 8
"""
sys.stdin = io.StringIO(_INPUT)

# ニムゲーム計算 grundyが0,1,2しかないので、前の石数から現在石数のgrundyが求まるがアルゴリズムが誤り続ける
# 模範解答のコピペ
# https://www.forcia.com/blog/002362.html

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

Amax = max(A)
# 各石の数のgrundyを算出
grundy = [[None] for j in range(Amax + 1)]


grundy[0] = 0
for i in range(1, Amax + 1):
    Transit = [False, False, False]
    if i >= X:
        # 前がどの0 ,1, 2から来たかで今回のbrundyが決まる
        Transit[grundy[i-X]] = True
    if i >= Y:
        # Yで上書きしてよい　ここに気付けなかった
        Transit[grundy[i-Y]] = True
    if Transit[0] == False:
        grundy[i] = 0
    elif Transit[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

# print(grundy)
# 出力
XOR_Sum = 0
for i in range(N):
    XOR_Sum = (XOR_Sum ^ grundy[A[i]])
if XOR_Sum >= 1:
    print("First")
else:
    print("Second")
