import io
import sys

_INPUT = """\
123 777
"""
sys.stdin = io.StringIO(_INPUT)

# ここから提出
# ユーグリッド互除法
A, B = map(int, input().split())

big = 0
small = 0
remainder = 999999999
quotient = 999999999
answer = 1
if A >= B:
    big = A
    small = B
else:
    big = B
    small = A

while quotient > 0:
    quotient ,remainder = divmod(big, small)
    # print(big, small, quotient, remainder)
    if remainder == 0:
        # print('p')
        answer = small
        break
    elif quotient == 0: break
    else:
        big = small
        small = remainder
print(answer)
