import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
123456789 123456789012345678
"""
sys.stdin = io.StringIO(_INPUT)

# A29と同門
# pow関数は十分速かった
a, b = map(int, input().split())
# 割る数
CONST_DIVISION = 10**9 + 7
ret = pow(a, b, CONST_DIVISION)
print(ret)
