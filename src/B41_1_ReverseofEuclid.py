import io
import sys

_INPUT = """\
5 2
"""
"""
変数 
x,y があり、最初は両方の値が1 です。以下の 2 種類の操作を何回か行うことで、変数 x の値を X, 変数 y の値を 
Y にする方法を求めてください。

x の値を x+y に変更する
y の値を x+y に変更する
ただし 
X と Y の最大公約数は 1 であるとします。

方針 逆算で大きいものから小さいものを引いていく
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など

x, y = map(int, input().split())

ans = []

ans.append((x, y))
while x > 1 or y > 1:
    if x > y:
        x = x - y
    else:
        y = y - x
    ans.append((x, y))
ans.pop()
print(len(ans))
for x, y in reversed(ans):
    print(str(x) + ' ' + str(y))
