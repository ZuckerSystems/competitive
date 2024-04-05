import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
15 30
6 9
9 10
2 9
9 12
2 14
1 4
4 6
1 3
4 14
1 6
9 11
2 6
3 9
5 9
4 9
11 15
1 13
4 13
8 9
9 13
5 15
3 5
8 10
2 4
9 14
1 9
2 8
6 13
7 9
9 15
"""
sys.stdin = io.StringIO(_INPUT)
"""
3: {2, 4, 5}
"""


# 処理開始
def formatA61(pos, lst):
    #print(pos, lst, len(lst))

    ret = str(pos) + ': {'
    if len(lst) == 0:
        ret = ret + '}'
    for i in range(len(lst)):

        ret = ret + str(lst[i])
        if i == len(lst) - 1:
            ret = ret + '}'
        else:
            ret = ret + ', '

    #print(ret)
    return ret


N, M = map(int, input().split())

route = [list() for j in range(N + 1)]
#print(route)
for i in range(0, M):
    A, B = map(int, input().split())
    route[A].append(B)
    route[B].append(A)

for i in range(1, N + 1):
    print(formatA61(i, route[i]))
