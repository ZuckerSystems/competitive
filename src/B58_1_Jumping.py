import io
import sys

_INPUT = """\
5 20 40
0 20 30 60 70
"""
"""
N 個の足場が横一列に並んでおり、左から順に 1 から N までの番号が付けられています。
足場 1 がスタート地点、足場 N がゴール地点であり、足場 i はスタート地点から Xi メートルの位置にあります。
あなたは 1 回で L メートル以上 R メートル以下の距離を右方向にのみジャンプできるとき、
スタートからゴールまで最小何回のジャンプで行けますか。ただし、与えられる入力において、スタートからゴールまで到達できることが保証されます。

DPで横に石の数とジャンプ数を記録しながらゴールするまでジャンプ
石から次行ける石は取得関数を作ったほうがいいかも

DP表で簡単に解けるが、TLE randam01のパターン。100000✕100000のDP表更新になり持たない
no2でセグメントツリーでまとめて処理するように変更
"""
sys.stdin = io.StringIO(_INPUT)

# 1-indexで実装する
import bisect

N, L, R = map(int, input().split())
X = [0] + list(map(int, input().split()))


def can_jump_pos(pos, X):
    l = bisect.bisect_left(X, X[pos] + L)
    r = bisect.bisect_right(X, X[pos] + R) - 1
    if l >= len(X):
        l = l - 1
    #print(pos, 'can:', l, r)
    return (l, r)


INF = 10**9 + 1
dp = [INF] * (N + 1)
goal = False

# 初回の飛べる位置のDPを更新
l, r = can_jump_pos(1, X)
for i in range(l, r + 1):
    dp[i] = 1
    if N == 2:
        print(1)
        exit(0)

pos = 2
while not goal:
    if dp[pos] == INF:
        pos += 1
        continue
    l, r = can_jump_pos(pos, X)
    for p in range(l, r + 1):
        #print('p', p)
        dp[p] = min(dp[pos] + 1, dp[p])
        if p == N:
            goal = True
    pos += 1
#print(dp)
print(dp[N])
