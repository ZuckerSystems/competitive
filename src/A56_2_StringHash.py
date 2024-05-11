import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
7 3
abcbabc
1 7 1 7
1 5 2 6
1 2 6 7
"""
sys.stdin = io.StringIO(_INPUT)
"""
substringした結果が同じかの判定問題
文字列ハッシュ値でハッシュ差計算するのが問題の名称からもわかる
最大200000文字のローリングハッシュで実装する必要あり。
ローリングハッシュのアルゴリズムは拾ってきたもの
"""
N, Q = map(int, input().split())
S = input()

base = 37
mod = 10**9 + 9
pw = None


# スニペット化TODO
# ローリングハッシュリストを作成
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


setup_pw(N)
sHash = rolling_hash(S)

print(sHash)
for i in range(Q):
    query = list(map(int, input().split()))
    # 0index開始なのでQueryの数字-1から取得する必要がある
    ab = get(sHash, query[0] - 1, query[1])
    cd = get(sHash, query[2] - 1, query[3])
    if ab == cd:
        print('Yes')
    else:
        print('No')
