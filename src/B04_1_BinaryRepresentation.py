import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
1101
"""
sys.stdin = io.StringIO(_INtdUT)
n = input()
ans = 0
for i in range(1, len(n) + 1):
    b = int(n[-i])
    x = 2**(i - 1)
    #print(b, x)
    ans += b * x
print(ans)
