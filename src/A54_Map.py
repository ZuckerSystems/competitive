import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
3
1 tanaka 49
1 suzuki 50
2 tanaka
"""
sys.stdin = io.StringIO(_INPUT)
"""
MAP(dict)
"""

Q = int(input())
gradeDict = dict()

for i in range(0, Q):
    Query = list(input().split())
    if Query[0] == '1':
        gradeDict[Query[1]] = int(Query[2])
    elif Query[0] == '2':
        print(gradeDict[Query[1]])
