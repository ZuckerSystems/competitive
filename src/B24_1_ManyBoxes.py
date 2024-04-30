import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
5
30 50
10 30
40 10
10 30
40 51
"""
sys.stdin = io.StringIO(_INPUT)
"""
N 個の箱があります。
i 個目の箱の縦の長さは Xi であり、横の長さは Yiです。
以下の 2 つの条件両方を満たすとき、箱 A を箱 B の中に入れることができます。

(箱 A の縦の長さ) < (箱 B の縦の長さ)
(箱 A の横の長さ) < (箱 B の横の長さ)
箱は最大で何重にすることができますか。
ただし、箱を回転させて縦の長さと横の長さを逆にする操作はできないものとします。
X昇順Y降順に並べてYを小さい順に並ぶかを検索する
"""
import bisect

N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]

#print(XY)
XY.sort(key=lambda x: (x[0], -x[1]))
#print(XY)

result = []
for i, xy in enumerate(XY):
    # 大きいものを右に押しやるようにresultを更新
    #print(XY[i][1])
    idx = bisect.bisect_left(result, XY[i][1])
    if idx == len(result):
        result.append(XY[i][1])
    else:
        #小さくなかった
        result[idx] = XY[i][1]
    #print(XY[i][1], result)

print(len(result))
