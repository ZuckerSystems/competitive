
import io
import sys

_INPUT = """\
5
2 4 1 3
5 3 7
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# 
import bisect
N = int(input())
A = list(map(int, input().split()))
B = [0] * list(map(int, input().split()))

# 算出用のMAPを作成する
for i in range(N):
  None

print(*B)

