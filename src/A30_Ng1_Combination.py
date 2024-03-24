
import io
import sys

_INPUT = """\
4 2
"""
sys.stdin = io.StringIO(_INPUT)

# 階乗計算はビットシフトで実現するがライブラリで十分
# お試しで再帰で
n, r = map(int, input().split())
# 割る数
CONST_DIVISION = 10 ** 9 + 7
# print(CONST_DIVISION)
def factorial_recursive(n: int) -> int:
    if n == 0: return 1
    return n * factorial_recursive(n - 1)

nf = factorial_recursive(n)
rf = factorial_recursive(r)
nMinusrf = factorial_recursive(n - r)

C = nf / (rf * nMinusrf)

ret = int(C % CONST_DIVISION)
print(ret)


