
import bisect
import io
import sys

_INPUT = """\
3
123 86399
1 86400
86399 86400
"""
sys.stdin = io.StringIO(_INPUT)

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
ans = 1
endTimeminIndex = 0
# endTimeMinValue = 86400
for i in range(N):
    endTime = LR[i][1]
    # endTimeMinValue = LR[i][1]
    for j in range(i, N):
        startTime = LR[j][0]
        if startTime >= endTime:
            endTime = LR[j][1]
            ans += 1

print(ans)
