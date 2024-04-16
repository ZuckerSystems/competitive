import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
5 65 7 37
5 15 30 50 55
"""
sys.stdin = io.StringIO(_INtdUT)
"""
川幅がW メートルである KYOPRO 川には、 N 個の足場が一直線上に並べられており、
西から順に 1 から N までの番号が付けられています。足場 i (1≤i≤N) は西岸から X i​  メートルの位置にあります。
太郎君は東方向のジャンプを繰り返すことで、西岸から東岸まで移動しようと思いました。
しかし、一回のジャンプで飛ぶ距離は長すぎても短すぎてもダメであり、 
L メートル以上 R メートル以下でなければなりません。移動方法は全部で何通りありますか。

解法）
石をノードに見立てて各ノードまでのルート数を算出しながらゴールする配るDPで
TLE N値が最大150,000✕150,000のループ処理になるため
区間累積和を取得するのはセグメント木が最適か
A58と問題の本質は変わっていない
"""


#####segfunc#####
def segfunc(x, y):
    return x + y


#################

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

    def add(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] += x
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


import bisect

n, w, l, r = map(int, input().split())
x = list(map(int, input().split()))
x.append(w)
x.insert(0, 0)

MOD = 10**9 + 7
segTree = SegTree([0] * n, segfunc, ide_ele)
segTree.add(0, 1)
segTree.add(1, -1)  # トップに1を入れるのでその下位には-1を入れておかないと合算値が増えすぎるため

for ids, i in enumerate(x):
    posL = i + l
    posR = i + r
    indexL = bisect.bisect_left(x, posL)
    indexR = bisect.bisect_right(x, posR)
    adding = segTree.query(0, ids + 1)

    segTree.add(indexL, adding)
    segTree.add(indexR, -adding)

print(segTree.query(0, n + 2) % MOD)
