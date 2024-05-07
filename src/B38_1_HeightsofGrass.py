import io
import sys

_INPUT = """\
288
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())


def calc_sum_digit(n):
    sumDigit = 0
    tmp = n
    while tmp > 0:
        tmp, mod = divmod(tmp, 10)
        sumDigit += mod
    return sumDigit


# 方針を変えて数字の繰り返し出現数で求める
# お数学になるので、暇なときに TODO
n = [int(x) for x in list(str(N))]

# 0-9までは45
# 0-99 までは 45 ** 10 * 2
# 0-999 までは 45 ** 100 * 3


def calc_dig(n):  #n桁までの9999.n桁までの合計 9999
    return 45 * 10**(n - 1) * n
