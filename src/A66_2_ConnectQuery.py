import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
12 12
2 9 11
1 1 7
1 1 4
2 3 6
1 3 5
2 3 5
1 10 12
1 4 8
1 8 11
2 10 12
1 5 9
2 6 8
"""
sys.stdin = io.StringIO(_INPUT)
"""
頂点数 
N のグラフに対して、以下の 2 種類のクエリを高速に処理してください。
クエリ 1：頂点 u と頂点 v を双方向に結ぶ辺を追加する。
クエリ 2：頂点 u と頂点 v は同じ連結成分に属するかを答える。
ただし、最初はグラフに辺が一本もなく、与えられるクエリの数は Q 個であるとします。

UnionFindで実装
"""


class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x  # x が根の場合は x を返す
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
        # union by rank
        if self.rank[rx] < self.rank[ry]:  # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]:  # rx 側の rank を調整する
            self.rank[rx] += 1
        return True

    # debug用
    def getPar(self):
        return self.par


n, q = map(int, input().split())
unionFind = UnionFind(n + 1)

for i in range(q):
    qy, u, v = map(int, input().split())
    if qy == 1:
        unionFind.unite(u, v)

    else:
        if unionFind.issame(u, v):
            print('Yes')
        else:
            print('No')
