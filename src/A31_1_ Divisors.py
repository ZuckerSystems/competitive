
import io
import sys

_INPUT = """\
30
"""
sys.stdin = io.StringIO(_INPUT)

#1 以上 N 以下の整数のうち、3,5のいずれかで割り切れるものは何個ありますか。

# 最小公倍数 ３✕5＝１５の内
# そのうち7はの約数

# 入力など
N = int(input())

ans = 0
q = 0
r = 0

q, r = divmod(N, 15)
ans = q * 7
# 余りだけ全件探索
for i in range(1,r + 1):
	if i % 3 == 0 or i % 5 == 0:
		ans = ans + 1

print(ans)