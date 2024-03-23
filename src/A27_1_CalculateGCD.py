import io
import sys

_INPUT = """\
1651 4381
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
print(i)
while i > 1:
  print(i)
  # if i == 1: break
  if small % i == 0:
     modmin = i / small #割り切れる
     if big % i == 0:
         answer = i
         break
     else:
        modmin = i / small #割り切れる
        i = int(i / modmin) + 1
  else:
     print('-')
     i -= 1
print(answer)

# 36 1 18 2 12 3 6