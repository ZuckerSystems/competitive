import io
import sys

_INPUT = """\
9999
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


#def calc_mod10(n):
#    return calc_sum_digit(n // 10)

ans = 0
j = 0
digVal = 0
for i in range(1, N + 1):
    if i % 10 == 0:
        j = 0
        digVal = sum(map(int, str(i)))
        #if calc_sum_digit(i) != digVal:
        #    print('NG', i, digVal)
        ans += digVal
    else:
        #print(i, digVal, j)
        j += 1
        #if calc_sum_digit(i) != digVal + j:
        #    print('NG', i, digVal, j)
        ans += digVal + j
print(ans)
