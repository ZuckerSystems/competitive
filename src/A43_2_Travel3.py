import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
1 23
4 W
"""
sys.stdin = io.StringIO(_INPUT)
"""
全長 L メートルの ALGO トンネルには、現在 N 人がいます。人 i は西端から Aiメートルの位置におり、方向Biへ歩いています（E のとき東、W のとき西）。
トンネルの幅は狭いため、2 人が同じ位置に来たら移動方向を変えます。全員が秒速 1 メートルで歩くとき、最後の人がトンネルの外に出るのは何秒後ですか。
"""
# 東向きの配列と西向きの最小差が最初に向きが変わる人
# 次の人にぶつかると向きを変えて反対側がゴールになるが、初期位置が一番遠かった人の値がそのまま解となる
# G E                                 W       G
# G                 EW                        G
# G                 WE                        G
# GW                                      E   G
# Eの人がゴールするのは初期のEの人のGまでの時間
N, L = map(int, input().split())
EAST = [L]
WEST = [0]
for i in range(N):
    A, B = input().split()
    if B == 'E':
        EAST.append(int(A))
    else:
        WEST.append(int(A))

maxE = L - min(EAST)
maxW = max(WEST)
sec = max(maxE, maxW)
print(sec)
