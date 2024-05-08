import io
import sys

_INPUT = """\
7
AABBBA
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
SList = [s for s in input()]

grass = [1] * N

# 加算を先に済ませる
for i in range(N - 1):
    if SList[i] == 'A':
        grass[i + 1] = grass[i] + 1

#print(grass)
#print(SList)
for i in range(N - 2, -1, -1):
    #rint(i)
    if SList[i] == 'B':
        grass[i] = max(grass[i], grass[i + 1] + 1)

print(sum(grass))
