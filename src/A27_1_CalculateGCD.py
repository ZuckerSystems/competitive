import io
import sys

_INPUT = """\
123 777
"""
sys.stdin = io.StringIO(_INPUT)

# ここから提出
# 試し割り法
A, B = map(int, input().split())

big = 0
small = 0
answer = 1
modmin = 0
if A >= B:
    big = A
    small = B
else:
    big = B
    small = A

i = int(small / 2) + 1
# print(i)
while i > 1:
    # print(i)
    # if i == 1: break
    if small % i == 0:
        modmin = i / small  # 割り切れる
        if big % i == 0:
            answer = i
            break
        else:
            if i == 2:
                break
            # 1260 の場合、630で割れる。
            # 次に探索するのは (1260/3)+1からでよい。3は2+1
            i = int(i / (modmin + 1)) + 1
    else:
        # print(i)
        i -= 1

print(answer)
