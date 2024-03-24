
import io
import sys

_INPUT = """\
77777 44444
"""
sys.stdin = io.StringIO(_INPUT)

def Division(a, b, m):
	# 数学論理は下記参照
	# https://algo-logic.info/combination/
	return (a * pow(b, m - 2, m)) % m

# 入力など
n, r = map(int, input().split())
M = 10**9 + 7

# 手順 1：分子を求める
a = 1
for i in range(1, n + 1):
	a = (a * i) % M

#print('a' + str(a))

# 手順 2：分母を求める
b = 1
for i in range(1, r+1):
	b = (b * i) % M
for i in range(1, n-r+1):
	b = (b * i) % M

#print('b' + str(b))
# 手順 3：答えを求める
print(Division(a, b, M))