import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
6 7
1 2 15
1 4 20
2 3 65
2 5 4
3 6 50
4 5 30
5 6 8
"""
sys.stdin = io.StringIO(_INPUT)
"""
重み付き無向グラフに対する最短経路問題を解いてください。 具体的には、以下のようなグラフが与えられるとき、頂点 
1 から各頂点までの最短経路長を求めてください。

・頂点数は N 、辺数は M である、
・i 番目の辺は頂点Ai​と頂点 Bi​を結び、長さはCi​である
・なお、以降の説明では、頂点1 から頂点 k までの最短経路長を dist[k] とします。
k 行目にはdist[k] の値を出力してください。 ただし、頂点 k まで移動できない場合は代わりに −1 と出力してください。

# アルゴリズム
ダイクストラ法をトポロジカルソートを優先度付きキュー（ヒープ）で実現する
距離側でソートした行き先をgraphとして用意(距離 , 行き先)※第２キーでソートするやり方が不明のため
・1→N ここは最短距離で確定、行ける先をキュー
・キューから距離順に取り出す
・N→M デキューして次の行き先を決めるこの時、1→Mへの距離が今までの最短の場合のみキューに入れておく
・キューから距離順に取り出す
・X→M のデキューが出てくるかもしれない。Mへの距離が短ければキューに入れる（可能性のあるルート）
"""

#import sys

#sys.setrecursionlimit(100000)  #再帰上限を上げる必要あり
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
    graph[A].append((C, B))  # 0-index
    graph[B].append((C, A))  # 0-index

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

for i in range(1, N + 1):
    if minDistanse[i] == INF:
        print(-1)
    else:
        print(minDistanse[i])
