import io
import sys

_INPUT = """\
30
"""
sys.stdin = io.StringIO(_INPUT)

#1 以上 N 以下の整数のうち、3,5,7 のいずれかで割り切れるものは何個ありますか。

# 最小公倍数 ３✕５✕７＝１０５　１０５の内
# そのうち５７個は３５７の約数

# 入力など
N = int(input())

ans = 0
q = 0
r = 0

q, r = divmod(N, 105)
ans = q * 57
# 余りだけ全件探索
for i in range(1, r + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        ans = ans + 1

print(ans)
