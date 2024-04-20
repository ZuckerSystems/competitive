import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
99999
"""

sys.stdin = io.StringIO(_INtdUT)

n = int(input())


def calc(x):
    return x**3 + x


min = 0
max = 100
mid = (min + max) / 2
x = calc(mid)
#print(x)
while abs(x - n) > 0.0001:
    if x - n > 0.0001:
        max = mid
    else:
        min = mid
    mid = (min + max) / 2
    x = calc(mid)
    #print(ans)
print(round(mid, 6))
