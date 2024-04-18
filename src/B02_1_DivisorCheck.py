import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
6 9
"""
sys.stdin = io.StringIO(_INtdUT)

a, b = map(int, input().split())
num = 100
l = [i for i in range(1, num + 1) if num % i == 0]
import numpy as np

l = np.array(l)
ans = np.where((l >= a) & (l <= b))
if len(ans[0]) == 0:
    print('No')
else:
    print('Yes')
