import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
6 7
1 2 5
1 4 4
2 3 4
2 5 7
3 6 3
4 5 3
5 6 5
"""
sys.stdin = io.StringIO(_INPUT)
"""
N 個のタンクと M 本のパイプがあります、j 本目のパイプはタンク A j​  からタンク B j​  の方向に毎秒 C j​  リットルまで水を流すことができます。
タンク 1 からタンク N まで毎秒最大何リットルの水を流すことができますか。ただし、タンクに水を貯めることはできないと考えてかまいません。

#題意がわからないので n = b の cを合計してみる
"""

n, m = map(int, input().split())
g = [0] * n
ans = 0
for i in range(m):
    a, b, c = map(int, input().split())
    if b == n:
        ans += c
print(ans)
