import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
3 3
1 2 70 1
2 3 20 1
1 3 90 0
"""
sys.stdin = io.StringIO(_INPUT)
"""
ALGO 市には N 個の交差点と M 本の道路があります。i 本目の道路は、交差点 Ai と交差点 Bi を双方向に結んでおり、長さは Ci メートルです。
交差点どうしは、いくつかの道路を通って必ず行き来できることが保証されます。
また、Di=1 であるような道路には、木が一本植えられています。
ALGO 市の市長である次郎君は、交差点 1 と交差点 N を結ぶマラソンコースを作ろうと思いました。
彼は参加者を疲れさせたくないので、合計距離をできるだけ短くしたいです。
また参加者に自然を楽しんでいただきたいので、合計距離が同じ場合、コース上に植えられている木の数をより多くしたいです。
どのようなマラソンコースが考えられますか。

幅優先探索で最短ルート探索しながら、同じ距離も許容し最も木が多いルートを残す
"""

import heapq

N, M = map(int, input().split())

INF = 10**9
X = 100000
minDistanse = [INF] * (N + 1)
graph = [[] for i in range(N + 1)]
priorityQueueDistance = []

# LISTで格納
for i in range(M):
    A, B, C, D = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    #dprint(A, B)
    graph[A].append((C * X - D, B))  # 0-index
    graph[B].append((C * X - D, A))  # 0-index

# 始点1からキューに入れていく

minDistanse[1] = 0
priorityQueueDistance = graph[1]
heapq.heapify(priorityQueueDistance)
while priorityQueueDistance:
    node = heapq.heappop(priorityQueueDistance)
    # 0が距離 1がnodeNo
    #print(node)
    #print(minDistanse[node[1]], node[1])
    # ここで枝切りをしておかないとTLE テストケース may_forget_continue.txt
    # 1からの距離順にソートしているため既にたどり着いているNodeはその先は算出不要
    if minDistanse[node[1]] != INF and node[1] != 0:
        #print(minDistanse[node[1]])
        continue
    else:
        minDistanse[node[1]] = node[0]
    nextNodes = graph[node[1]]
    for n in nextNodes:
        # 現在の距離と次への距離を足したものが既に算出済の次のノードの最短距離より短い場合
        if minDistanse[node[1]] + n[0] < minDistanse[n[1]]:
            # 現在の距離と次の距離を足したタプルをエンキュー 1からの距離順ってことになる
            #print('現在-距離-次')
            #print(node[1], minDistanse[node[1]] + n[0], n[1])
            heapq.heappush(priorityQueueDistance,
                           (minDistanse[node[1]] + n[0], n[1]))
tree = 0

if minDistanse[N] % X != 0:
    tree = X - (minDistanse[N] % X)

print(str(int((minDistanse[N] + tree) / X)) + ' ' + str(tree))
