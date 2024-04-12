import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
6 6
1 4
2 3
3 4
5 6
1 2
2 4
"""
sys.stdin = io.StringIO(_INPUT)
"""
N 頂点 M 辺の無向グラフが与えられます。各頂点には 1 から N までの番号が付けられており、i 番目の辺は頂点 A i​  と頂点 B i​  を結んでいます。
1 以上 N 以下の全ての整数 k について、以下の問いに答えてください。

頂点 1 から頂点 k まで、辺を何本かたどって移動することを考えるとき、
たどるべき辺の本数の最小値を出力せよ。ただし、移動不可能な場合は −1 を出力せよ。

幅優先探索で実装する
"""

N, M = map(int, input().split())
graph = {i: set() for i in range(N)}
#print(graph)

# 重複をなくすためセットを利用する 速度によってはListにしてループさせてもよいかも
for i in range(M):
    A, B = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    graph[A - 1].add(B - 1)  # 0-index
    graph[B - 1].add(A - 1)  # 0-index

#print(graph)

from collections import deque


# 幅優先探索
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    # print(queue)
    while queue:
        (node, path) = queue.popleft()
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    queue.append((child, path + [child]))
                    # print(queue)


# i = 0の場合0と解答する例外を先に処理
print(0)
for i in range(2, N + 1):

    result = bfs(graph, 0, i - 1)
    if result is not None:
        print(len(result) - 1)
    else:
        print(-1)
    #print(result)
