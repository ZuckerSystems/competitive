import io
import sys

_INPUT = """\
3 -4 1
"""
"""
黒板に 3 つの整数 a,b,c が書かれています。「3 つ中 2 つの整数を選び、片方に +1、もう片方に 
-1 する」という操作を何回か行い、書かれた整数を全部 0 にすることはできますか。

足し算するだけ？
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
a, b, c = map(int, input().split())

if a + b + c == 0:
    print('Yes')
else:
    print('No')
