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
ローリングハッシュ版 A56参照 速度は変わらず
"""
sys.stdin = io.StringIO(_INPUT)

base = 37
mod = 10**9 + 9
pw = None


# スニペット化TODO
# ローリングハッシュリストを作成 1-index
def rolling_hash(s):
    l = len(s)
    h = [0] * (l + 1)
    v = 0
    for i in range(l):
        h[i + 1] = v = (v * base + ord(s[i])) % mod
    return h


# RH前に、必要な長さの最大値分のpow-tableを計算しておく
def setup_pw(l):
    global pw
    pw = [1] * (l + 1)
    v = 1  #初期値
    for i in range(l):
        pw[i + 1] = v = v * base % mod


# ハッシュ値の差分算出
def get(h, l, r):
    return (h[r] - h[l] * pw[r - l]) % mod


def getRev(h, l, r):
    l, r = N + 1 - r, N + 1 - l
    return (h[r] - h[l] * pw[r - l]) % mod


N, Q = map(int, input().split())
S = input()
setup_pw(N)
sHash = rolling_hash(S)
sRevHash = rolling_hash(S[::-1])
for i in range(Q):
    l, r = map(int, input().split())
    if get(sHash, l, r) == getRev(sRevHash, l, r):
        print('Yes')
    else:
        print('No')
