import io
import sys

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
"""
頂点数 N、辺数 M の連結なグラフが与えられます。 
このグラフについて、頂点 1 から頂点 N までの単純パスを一つ出力してください。

幅優先探索
単方向なのでA62と違いリストで作成する. 単方向ではなかったもよう
routeを辿れるようにする
"""
sys.stdin = io.StringIO(_INPUT)

#import sys

sys.setrecursionlimit(100000)  #再帰上限を上げる

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
#print(graph)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

visited = [False for _ in range(N + 1)]
preVisit = [None for _ in range(N + 1)]


# 深さ優先探索
def dfs(graph, start, visited, preVisit):
    visited[start] = True
    for next_node in graph[start]:
        if visited[next_node]:
            continue
        preVisit[next_node] = start
        dfs(graph, next_node, visited, preVisit)
    return


dfs(graph, 1, visited, preVisit)

#print(visited)
#print(preVisit)
route = [N]
pos = N
while True:
    #print(preVisit[pos], pos)
    route.append(preVisit[pos])
    pos = preVisit[pos]
    if pos == 1:
        break
#print(route)
route.reverse()
print(*route)
