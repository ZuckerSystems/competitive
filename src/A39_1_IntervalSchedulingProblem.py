import io
import sys

#print(sys.getrecursionlimit())
_INPUT = """\
5
1 10
11 20
13 15
12 18
16 21
"""
sys.stdin = io.StringIO(_INPUT)

# 映画を見れる回数を返却する
# 再帰で記述すると再帰上限数に引っかかる


def WatchMovie(movieList: list, sttTime: int, pos: int, cnt: int):
    # print(j, movieList[1999][0])
    for i in range(pos, len(movieList)):
        # print(movieList[i])

        if movieList[i][0] >= sttTime:
            cnt += 1
            sttTime = movieList[i][1]

    return cnt


N = int(input())
LR = [0] * N
for i in range(N):
    LR[i] = list(map(int, input().split()))

# print(LR)
# 終了時間線を引く
# 1     |
# 2          |
# 3                   |
# 4   |
# 5        |
# 6             |
# 7                       |
# 開始時間がどうであれ、終了時間が早ければ次の終了時間が早いものを観られる
# 1→2→7であれば4→2→7の方が効率がよい1で2が見れたなら4→2も成立する

LR.sort(key=lambda x: x[1])

endTime = LR[0][1]
# print(LR, endTime)
ans = 1
ans = WatchMovie(LR, endTime, 1, ans)
print(ans)
