
import io
import sys

_INPUT = """\
3
3 5 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

# 最初の2個のパターンが
# (1, 1) Second
# (1, 2以上) First
# (N , N) First
# (N , M) Second
# 2進数表記にしたときに各桁を10進として足した値が偶数なら必勝型
# https://manabitimes.jp/math/950

nim = A[0]
for i in range(1, N):
    nim = nim ^ A[i]
ans = 'Second'
if nim > 0:
    ans = 'First'
print(ans)
