
import io
import sys

_INPUT = """\
5 23
"""
sys.stdin = io.StringIO(_INPUT)

# pow関数は十分速かった
a, b = map(int, input().split())
# 割る数
CONST_DIVISION = 10 ** 9 + 7
ret = pow(a, b, CONST_DIVISION)
print(ret)


