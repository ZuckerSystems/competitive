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
拡張点のnodeにこれから行ける場所と距離を保持する。
また、自分に到着したときの距離の最短を保持する。
頂点１距離０から再帰全探索する
A B C が 1 3 5と与えられた場合、3→1へは移動できない想定
→双方向移動可能なため作り直し
→距離がオーバするルートの枝切りのみ
→TLEとMLEになるので構造・アルゴリズムから作り直し MLEがなければタプルソートでもよいかも
"""

import sys

sys.setrecursionlimit(100000)  #再帰上限を上げる必要あり
N, M = map(int, input().split())

INF = 10**9


# 各ノードのクラス
class Node():

    def __init__(self, nodeNo, INF) -> None:
        self.nodeNo = nodeNo  # 自分自身のNo
        self.nextNodeWithDistanse = []  # 行き先と距離のタプル配列
        self.minDistanse = INF  # 自分自身が呼ばれた際の距離の最小値
        self.route = []  # 既に一度来たルート

    # 自分自身のnode番号を返す
    def getNodeNo(self):
        #print('id nodeNo=', id(self.nodeNo))
        return self.nodeNo

    # 次に行けるNodeを管理(nexNodeはタプルで)
    def addNextNode(self, nextNodeWithDistanse):
        #print('id nextnode=', id(self.nextNodeWithDistanse))
        self.nextNodeWithDistanse.append(nextNodeWithDistanse)

    def getNextNodes(self):
        return self.nextNodeWithDistanse

    # ディスタンスをセットする どこから来たかは問わない
    def setMinDist(self, distance):
        self.minDistanse = min(self.minDistanse, distance)

    # 最短距離を返す
    def getMinDistanse(self):
        return self.minDistanse

    #
    def setRoute(self, route):
        self.route.append(route)


## node管理用
nodes = dict()
# Nodes初期化する
# 実態に合わせるために1-indexで
for i in range(1, N + 1):
    node = Node(i, INF)
    nodes[i] = node

# Nodeクラスに距離や次のNodeをセットする
for i in range(M):
    A, B, C = map(int, input().split())
    #print('A', A)
    nodes[A].addNextNode((B, C))
    nodes[B].addNextNode((A, C))


# 前のノードから距離をもらって次のノードを再帰呼び出し
def bfsWithMinDistance(nextNode, distance):
    node = nodes[nextNode]
    node.setMinDist(distance)
    nextNodes = node.getNextNodes()
    #print(nextNodes)
    for next, nextDistance in nextNodes:
        #print(next, nextDistance)
        # 双方向行けるとくるくる回るが距離が遠くなったら止める
        if nodes[next].getMinDistanse() >= distance + nextDistance:
            bfsWithMinDistance(next, distance + nextDistance)

    return


# 処理開始 初期位置0 距離0
bfsWithMinDistance(1, 0)

for key in nodes.keys():
    node = nodes[key]
    distance = node.getMinDistanse()
    if distance == INF:
        distance = -1
    print(distance)
"""
# debug
print(nodes.keys())
for key in nodes.keys():
    node = nodes[key]
    print(node.getNodeNo(), node.getNextNodes())

print('-----------')
"""
