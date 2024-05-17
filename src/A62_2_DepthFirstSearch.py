import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
"""
もしグラフ全体が連結であれば、 The graph is connected. と出力する
そうでなければ、 The graph is not connected. と出力する
グラフが与えられているので 深さ優先探索DFSで実装する
再帰上限を上げられる事を知らずにfor分で実現しようとしたが、再帰上限上げるのみでOKでした
"""
import sys

sys.setrecursionlimit(100000)  #再帰上限を上げる必要あり

N, M = map(int, input().split())
graph = {i: set() for i in range(N)}
#print(graph)

# 重複をなくすためセットを利用する　速度によってはListにしてループさせてもよいかも
for i in range(M):
    A, B = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    graph[A - 1].add(B - 1)
    graph[B - 1].add(A - 1)

#print(graph)


# 深さ優先探索
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited


visited = dfs(graph, 0)

if len(visited) == N:
    print('The graph is connected.')
else:
    print('The graph is not connected.')
