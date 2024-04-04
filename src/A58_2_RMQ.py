import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
8 4
1 3 16
2 4 7
1 5 13
2 4 7
"""
sys.stdin = io.StringIO(_INPUT)
"""
長さ N の数列A=(A1 ,A2 ,…,AN) があり、最初はすべての要素が 
0 になっています。以下の 2 種類のクエリを処理してください。
クエリ 1：Apos  の値をx に更新する。
クエリ 2：Al ,Al+1 ,…,Ar−1の最大値を答える。
セグメント木で解く
→区間検索がうまくいかず
"""


class RMQSegmentTree:
    #
    tree = []  #セグ木の実態
    n = 0  #セグ木の上位段の数 変数名がイケてない

    # treesize = 0 # セグ木の実際の数
    def __init__(self, elementCount) -> None:
        # コンストラクタで初期化する。
        self.n = 1

        # 最下段の数を求める2の倍数とする
        while self.n < elementCount:
            self.n *= 2
            #print('必要な要素数算出', self.n, elementCount)

        # 最下段の２倍が木の要素数を初期化 0indexにしたいので
        self.tree = [0] * (self.n * 2 - 1)
        #print(self.tree)

    # elementCountが8の場合こういうインデックスのツリーとする
    #[              0               ]
    #[      1       ][       2      ]
    #[   3  ][   4  ][  5   ][  6   ]
    #[ 7][ 8][ 9][10][11][12][13][14]
    def update(self, idx, num):
        # idx = 0 の時 tmpidx=7 となるか
        tmpidx = idx + self.n - 1
        #print('idx', idx, 'tmpidx', tmpidx, self.n)
        self.tree[tmpidx] = num
        while tmpidx > 0:
            tmpidx = (tmpidx - 1) // 2
            # 上位は2で割ったもの。偶数の場合は右と比較。奇数は左
            self.tree[tmpidx] = max(self.tree[2 * tmpidx + 1],
                                    self.tree[2 * tmpidx + 2])

        #print(self.tree)
        #for i in range(len(self.tree)):
        #    print(i, self.tree[i])
        #return

    # 要求区間 [a, b) 中の要素の最小値を答える
    # k := 自分がいるノードのインデックス
    # 対象区間は [l, r) にあたる
    # 初回呼び出しはm=0 l=0 r= -1
    def getMAX(self, a, b, k, l, r) -> int:
        # 最上段の範囲 [7-14→0-7に変換して比較している]
        # 全範囲カバーするように２分割再帰しながら下段に降りていく
        # 初回呼び出し時のrは最下段配列数
        # print(a, b, k, l, r)
        #print(k)
        if r < 0:
            r = self.n - 1
            # print('初回', a, b, k, l, r)
        # 対象範囲外
        if r <= a or b <= l:
            # print('対象範囲外', a, b, k, l, r)
            return -10000
        # 要求区間をすべてカバーしている
        if l >= a and b >= r:
            # print(self.tree[k])
            return self.tree[k]

        # 子のカバー範囲を与えて再帰
        #print('Left:', a, b, 2 * k + 1, l, (l + r) // 2)
        #print('right:', a, b, 2 * k + 2, (l + r) // 2 + 1, r)

        lMax = self.getMAX(a, b, 2 * k + 1, l, (l + r) // 2)
        rMax = self.getMAX(a, b, 2 * k + 2, (l + r) // 2 + 1, r)

        #print(a, b, k, 'l', l, 'r', r, lMax, rMax)
        return max(lMax, rMax)


# 処理開始
N, Q = map(int, input().split())
segmentTree = RMQSegmentTree(N)

for i in range(Q):

    query = list(map(int, input().split()))
    # 0index開始なのでQueryの数字-1から取得する必要がある
    if query[0] == 1:
        segmentTree.update(query[1] - 1, query[2])

    elif query[0] == 2:
        print(segmentTree.getMAX(query[1] - 1, query[2] - 1, 0, 0, -1))
