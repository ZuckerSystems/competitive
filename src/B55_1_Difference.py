import io
import sys

_INPUT = """\
5
2 -30
1 -10
2 -30
1 -40
2 -30
"""
"""

"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
import bisect

Q = int(input())
hands = []
for i in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        #print(x)
        bisect.insort_left(hands, x)
        #print(hands)
    else:
        if hands:
            indexLeft = bisect.bisect_left(hands, x)
            indexRight = bisect.bisect_right(hands, x)
            #print(hands, x, indexLeft, indexRight, len(hands))
            if indexRight == len(hands):
                r = 10**9 + 1
            else:
                r = abs(hands[indexRight] - x)
            if indexLeft == 0:
                l = 10**9 + 1
            else:
                l = abs(x - hands[indexLeft - 1])
            print(min(r, l))
        else:
            print(-1)
