import io
import sys

_INPUT = """\
12 3
mississippia
5 8
6 10
2 8
"""
"""
回文とは、前から読んでも後ろから読んでも変わらない文字列のことを指します。たとえば abba や level は回文です。

長さ 
N の文字列 S が与えられます。以下の Q 個のクエリに答えてください。
i 個目のクエリ:S[Li,Ri] は回文か？
ただし、S[l,r] は S の l 文字目から r 文字目までの連続部分文字列のことを指します。

回文の高速判定は拾ってきたもの
StringHashの正順、逆順を作成するパターンと比較してみる
"""
sys.stdin = io.StringIO(_INPUT)


# 入力など
#回文か判定するクラス拾い物 https://qiita.com/klattimia/items/3cbe4f702e2f20761f0d
class Manacher:

    def __init__(self, l):
        self.n = len(l)
        self.m = 2 * self.n + 1
        self.d = ['&'] * self.m
        self.r = [0] * self.m
        for i in range(self.n):
            self.d[2 * i + 1] = l[i]
        self.make_r()

    def make_r(self):
        i, j = 0, 0
        while i < self.m:
            while j <= i < self.m - j and self.d[i - j] == self.d[i + j]:
                j += 1
            self.r[i] = j
            k = 1
            while k <= i < self.m - k and k + self.r[i - k] < j:
                self.r[i + k] = self.r[i - k]
                k += 1
            i += k
            j -= k

    def judge(self, start, end):
        center = start + end
        return 2 * end - 1 < center + self.r[center]


N, Q = map(int, input().split())
S = input()

s = Manacher(S)

for i in range(Q):
    l, r = map(int, input().split())
    ans = s.judge(l - 1, r)
    print('Yes' if ans == True else 'No')
