import io
import sys

_INPUT = """\
10 2
101001000011000100010111
000010011110110010100111
101110001110000011110111
011011110100011110100011
000011001111111010110001
001010011010101010110100
001010010111101101111010
110011111100010110111011
100010011100011101110001
010110100101101111111011
"""
"""
YOPRO 工場には N 人の社員が在籍しています。しかし、社員が全時間帯に勤務できるとは限りません。社員 
i が働ける時間の情報は C i  で表され、j 時台 (0≤j≤23) に働けるとき C i,j =1、
働けないとき C i,j =0 となります。
また、社員をあまりに働かせると、ブラック企業という評価を受けてしまうため、どの社員も一日 
10 時間までしか勤務させてはいけません。このような条件下で、どの時間帯にも 
M 人以上が勤務しているようにシフトを組むことは可能かどうかを判定してください。

MaxFlowのアルゴリズムで解く問題だと思うが制約10時間をどのように対応するか

流量1キャパシティ10にして算出する
edgeが24なのでnodeは24+2
キャパシティと流量付きのMaxFlowアルゴリズムをコピペ
"""
sys.stdin = io.StringIO(_INPUT)
"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bp

point
■1.1つのマッチングと、s->tの流量=1であることが対応する。
■2.マッチングできない時は水を流せない=辺を貼れない
■3.例えば複数人から一つの椅子に辺が伸びている時も、結局一人しか座れない。
これは椅子からtへの辺の容量が1になっているため、複数人からの辺があっても
結局一人分の水しか流せないため。

■4.今回、一人10時間までしか働くことができないので、sから各個人に流れる流量は
10とする。
■5.各時間帯について、1人1時間までしか働くことができないので、個人から時間帯へ
流れる流量は1とする
■6.各時間帯において、最低でもm人が必要で、m人以上になってもよい。これは
各時間帯からtへ伸びた辺のcapacityがmであり、tに流れる流量が24*mになっていれば、
各時間帯においてm人以上の労働者がいたことになる。
→一つの時間帯でもm人未満の場合は、時間帯->tへの辺の流量がm未満になるため、
tへ流れる流量の合計が絶対に24*mに到達しない.
"""
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter


def II():
    return int(input())


def IS():
    return input().rstrip()


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, input().split()))


def MS():
    return input().rstrip().split()


def LS():
    return list(input().rstrip())


from string import ascii_lowercase, ascii_uppercase  # alphabet list
from itertools import combinations, permutations, product

if sys.platform == 'ios':
    import clipboard
    a = clipboard.get()
    a = a.split('\n')
    text = '\n'.join(a)
    with open('input_file.txt', 'w') as f:
        f.write(text)
    sys.stdin = open('input_file.txt')


# Ford-Fulkerson algorithm
# https://tjkendev.github.io/procon-library/python/max_flow/ford-fulkerson.html
class FordFulkerson:

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    # 各辺について、fr:始点、to:行き先、cap:辺の重み
    # G[v] := (行き先,辺の重み,逆辺=(fr,逆辺の重み,None))
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF = 10**9 + 7
        N = self.N
        while f:
            self.used = [0] * N
            f = self.dfs(s, t, INF)
            flow += f
        return flow


def solve():
    n, m = MI()
    ff = FordFulkerson(n + 24 + 2)
    s = n + 24
    t = n + 24 + 1

    for i in range(n):
        ff.add_edge(s, i, 10)
        c = IS()
        for j in range(24):
            if c[j] == "1":
                ff.add_edge(i, n + j, 1)

    for j in range(24):
        ff.add_edge(j + n, t, m)

    if ff.flow(s, t) == 24 * m:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
