import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
1 5
2 1 2
1 1 5
2 1 2
1 1 3
2 1 2
"""
sys.stdin = io.StringIO(_INPUT)
"""
長さ N の数列A=(A1 ,A2 ,…,AN) があり、最初はすべての要素が 
0 になっています。以下の 2 種類のクエリを処理してください。
クエリ 1：Apos  の値をx に更新する。
クエリ 2：Al ,Al+1 ,…,Ar−1の最大値を答える。
セグメント木で解く
クラスを拾ってくる(キータからhttps://qiita.com/takayg1/items/c811bd07c21923d7ec69)
from atcoder.lazysegtree import LazySegTree というライブラリもある。競技プログラミング用ライブラリのため使用はしない
"""


#####segfunc#####
def segfunc(x, y):
    return max(x, y)


################

#####ide_ele#####
ide_ele = 0
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

        #print(self.tree)

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


# 処理開始
N, Q = map(int, input().split())

leaf = [0] * (N)
segTree = SegTree(leaf, segfunc, ide_ele)
for i in range(Q):

    query = list(map(int, input().split()))
    # 0index開始なのでQueryの数字-1から取得する必要がある
    if query[0] == 1:
        segTree.update(query[1] - 1, query[2])

    elif query[0] == 2:
        ret = segTree.query(query[1] - 1, query[2] - 1)
        print(ret)
