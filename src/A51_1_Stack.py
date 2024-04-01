import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
5
1 futuremap
1 howtospeak
2
3
2
"""
sys.stdin = io.StringIO(_INPUT)
"""
先入れ後出しのStackを実装する。
といっても標準listにその機能がある。また件数が多い場合はライブラリを利用する。
"""
Q = int(input())
stack = []
for i in range(0, Q):
    Query = list(input().split())
    if Query[0] == '1':
        stack.append(Query[1])
    elif Query[0] == '2':
        print(stack[-1])
    elif Query[0] == '3':
        stack.pop()
