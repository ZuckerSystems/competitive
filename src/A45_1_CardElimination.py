import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
4 B
WBBR
"""
sys.stdin = io.StringIO(_INPUT)

N, C = input().split()
N = int(N)
A = list(input())  # Nまでのリスト


# この問題数パターンためしてもどこから算出しても答えが変わらないので左から算出する方針で
# ニムとも違うが定められた変化パターンが二項演算で結果が定まるパターンの模様
# プログラムアルゴリズムの問題としてはいまいち
def changeColor(x, y):
    if x == 'W' and y == 'W':
        return 'W'
    if x == 'B' and y == 'B':
        return 'R'
    if x == 'R' and y == 'R':
        return 'B'
    if x == 'W' and y == 'B' or x == 'B' and y == 'W':
        return 'B'
    if x == 'W' and y == 'R' or x == 'R' and y == 'W':
        return 'R'
    if x == 'B' and y == 'R' or x == 'R' and y == 'B':
        return 'W'


for i in range(1, N):
    A[i] = changeColor(A[i - 1], A[i])

if A[N - 1] == C:
    print('Yes')
else:
    print('No')
