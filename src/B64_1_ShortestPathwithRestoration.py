import io
import sys

_INPUT = """\
15 4
10 15 18
1 10 19
6 10 18
6 15 25
"""
"""
頂点数 N、辺数 M の重み付き無向グラフが与えられます。 
頂点 1 から頂点 N までの具体的な最短経路を 1 つ出力してください。 
計算量は O(MlogN) であることが望ましいです。
"""
sys.stdin = io.StringIO(_INPUT)
import heapq

N, M = map(int, input().split())

INF = 10**9

minDistanse = [INF] * (N + 1)
graph = [[] for i in range(N + 1)]
priorityQueueDistance = []

# LISTで格納
for i in range(M):
    A, B, C = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    #dprint(A, B)
    graph[A].append((C, B, A))  # 0-index
    graph[B].append((C, A, B))  # 0-index

# 始点1からキューに入れていく
preVisit = [None for _ in range(N + 1)]
minDistanse[1] = 0
priorityQueueDistance = graph[1]
heapq.heapify(priorityQueueDistance)
while priorityQueueDistance:
    node = heapq.heappop(priorityQueueDistance)
    #print(node)
    # 0が距離 1がnodeNo
    #print(node)
    #print(minDistanse[node[1]], node[1])
    # ここで枝切りをしておかないとTLE テストケース may_forget_continue.txt
    # 1からの距離順にソートしているため既にたどり着いているNodeはその先は算出不要
    if minDistanse[node[1]] != INF and node[1] != 0:
        #print('skip-', node)
        #print(minDistanse[node[1]])
        continue
    else:
        minDistanse[node[1]] = node[0]
        preVisit[node[1]] = node[2]
    #if node[1] == N:
    #    break
    nextNodes = graph[node[1]]
    for n in nextNodes:
        # 現在の距離と次への距離を足したものが既に算出済の次のノードの最短距離より短い場合
        if minDistanse[node[1]] + n[0] < minDistanse[n[1]]:
            # 現在の距離と次の距離を足したタプルをエンキュー 1からの距離順ってことになる
            #print('現在-距離-次')
            #print(node[1], minDistanse[node[1]] + n[0], n[1])
            #print(node[1], n[1], minDistanse[node[1]], minDistanse[n[1]])
            heapq.heappush(priorityQueueDistance,
                           (minDistanse[node[1]] + n[0], n[1], node[1]))

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
