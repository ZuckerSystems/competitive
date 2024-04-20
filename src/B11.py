import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
15
83 31 11 17 32 19 23 37 43 47 53 61 67 5 55
5
10
20
30
40
50
"""

sys.stdin = io.StringIO(_INtdUT)

import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
a.sort()
#print(a)
for i in range(q):
    print(bisect.bisect_left(a, int(input())))
