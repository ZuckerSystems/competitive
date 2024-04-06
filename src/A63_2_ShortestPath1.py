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

幅優先探索で実装する。一度全距離探索を行い、最短で出てきた数字をメモしておく
TODO: setに見直ししたい
"""

N, M = map(int, input().split())
graph = [[] for i in range(N)]
#print(graph)

# LISTで格納
for i in range(M):
    A, B = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    #dprint(A, B)
    graph[A - 1].append(B - 1)  # 0-index
    graph[B - 1].append(A - 1)  # 0-index


# 幅優先探索で全てのnodeの最短を算出
def bfs(graph, max_node):

    # 各頂点が何手目に探索されたか
    # -1 は「まだ探索されていない」ことを表す
    visited = [-1] * (max_node + 1)
    # k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
    nodes = [[] for i in range(max_node)]

    # 頂点 0 を始点とする
    visited[0] = 0
    nodes[0] = [0]
    # k 手目の探索をする
    for k in range(1, max_node):
        # k-1 手目に探索された各頂点 v に対して
        for v in nodes[k - 1]:
            # 頂点 v から 1 手で行ける頂点 next_v を探索
            for next_v in graph[v]:
                # 頂点 next_v が探索済みであれば何もしない
                if visited[next_v] != -1:
                    continue

                # 頂点 next_v を探索する
                visited[next_v] = visited[v] + 1
                #print(k, next_v)
                nodes[k].append(next_v)
    return visited


visited = bfs(graph, N)
# i = 0の場合0と解答する例外を先に処理
print(0)
for i in range(1, N):

    print(visited[i])
