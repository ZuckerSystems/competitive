import io
import sys

_INPUT = """\
7 9
1 2 12
1 3 10
2 6 160
2 7 15
3 4 1
3 5 4
4 5 3
4 6 120
6 7 14
"""
"""
最大全域木の長さ
A67を最大に変更するのみ
#--------------------------------#
https://algo-method.com/tasks/1011/editorial
"""
sys.stdin = io.StringIO(_INPUT)

import sys

sys.setrecursionlimit(100000)  #再帰上限を上げる


# 辺情報を表す構造体
class edge:

    def __init__(self, start, end, leng):
        self.start = start  # 辺の始点
        self.end = end  # 辺の終点
        self.leng = leng  # 辺の重み

    # 構造体 edge の比較関数
    def __lt__(self, other):
        #return self.leng < other.leng 最小ならこちら
        return self.leng > other.leng  #最大全域木


# Union-Find
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        for i in range(n):
            self.par[i] = i
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == x: return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False  # すでに同じグループのときは何もしない
        # union by size
        if self.siz[rx] > self.siz[ry]:  # ry 側の siz が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        self.siz[rx] += self.siz[ry]  # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


# main
# 入力を受け取る
N, M = map(int, input().split())
graph_edges = [[] for _ in range(M)]  # graph_edges[i]：i 番目の辺情報
for i in range(M):
    u, v, w = map(int, input().split())
    graph_edges[i] = edge(u, v, w)

# 辺情報を重みの昇順にソートする
graph_edges.sort()
# 要素数 N の Union-Find を用意する
uf = UnionFind(N + 1)

ans = 0  # 答えとなる変数
for i in range(M):
    # 重みが i 番目に小さい辺は、頂点 u, v を結ぶ、重み w の辺であるとする
    u, v, w = graph_edges[i].start, graph_edges[i].end, graph_edges[i].leng

    #print(w)
    # 頂点 u, v がすでに同じグループに属するなら、この辺は採用しない
    if uf.issame(u, v): continue
    # そうでないなら、この辺を採用する
    # Union-Find 上で u, v を統合して、答えに w を足す
    uf.unite(u, v)
    ans += w
# 答えを出力する
print(ans)
