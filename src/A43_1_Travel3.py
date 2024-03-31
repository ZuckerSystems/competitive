import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
3 100
20 E
50 E
70 W
"""

#
sys.stdin = io.StringIO(_INPUT)
"""
全長 L メートルの ALGO トンネルには、現在 N 人がいます。人 i は西端から Aiメートルの位置におり、方向Biへ歩いています（E のとき東、W のとき西）。
トンネルの幅は狭いため、2 人が同じ位置に来たら移動方向を変えます。全員が秒速 1 メートルで歩くとき、最後の人がトンネルの外に出るのは何秒後ですか。
"""
# 可視化して１秒毎の様子を見てみたいのでそのように実装
# もちろんTLE,REにいくつかなります

N, L = map(int, input().split())
A = [None] * N  # 人
B = [None] * N  # 方向
for i in range(N):
    A[i], B[i] = input().split()
    A[i] = int(A[i])


# マップを見るデバッグ用
def ShowMAP(MAP, sec):
    for i in range(L + 2):
        if sum(MAP[i]) > 0:
            print(sec, i, MAP[i])


def chageDirection(i, E, W):
    for j in range(N):
        if MAP[i][j] == E:
            MAP[i][j] = W
        elif MAP[i][j] == W:
            MAP[i][j] = E


# 可視化して１秒毎の様子を見てみたいのでそのように実装
MAP = [[0 for j in range(N)] for i in range(L + 2)]

# Eはマイナス Wはプラス
for j in range(N):
    direction = 0
    if B[j] == 'E': direction = 3
    elif B[j] == 'W': direction = 2
    MAP[A[j]][j] = direction

#ShowMAP(MAP, 0)
cnt = 0
move = -1
while move != 0:
    move = 0
    cnt += 1
    W = 2
    if cnt % 2 == 0:
        E = 4
        Enext = 3
    else:
        E = 3
        Enext = 4
    for i in range(L + 1):
        for j in range(N):
            if MAP[i][j] == E:
                if i < L:
                    MAP[i + 1][j] = Enext
                    MAP[i][j] = 0
                    move += 1
            elif MAP[i][j] == W:
                if i < L and i > 0:
                    MAP[i - 1][j] = W
                    MAP[i][j] = 0
                    move += 1

    # 1秒進んだところで出会った人を反転
    for i in range(L + 1):
        if sum(MAP[i]) >= 5:
            #print('Enext', Enext)
            #ShowMAP(MAP, cnt)
            chageDirection(i, Enext, W)
            #ShowMAP(MAP, cnt)
        #ShowMAP(MAP, cnt)

    if move == 0:
        cnt -= 1  #最後は動かしていない
        break

#ShowMAP(MAP, cnt)
print(cnt)
