import io
import sys

_INPUT = """\
7
3 6 4 5 7 1 2
"""
"""
3 6 4 5 7 1 2
1からNまでがランダムに並んでいる中で A > Bになる組わせの数を求める

# 全幅探索で普通に解く NG
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] - A[j] > 0:
            ans += 1

print(ans)
