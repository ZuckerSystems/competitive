import io
import sys

_INPUT = """\
15 1
1 2
2 3
1 4
1 5
1 6
6 7
2 8
6 9
9 10
10 11
6 12
12 13
13 14
12 15
"""
"""
株式会社 KYOPRO-MASTER には N (≤100000) 人の社員がおり、1 から N までの番号が付けられています。 
ライバル会社に勤務している太郎君は、以下の N-1 個の情報を入手しました。
i 個目の情報: 社員 Ai と社員 Bi は直属の上司と部下の関係にある。
ここで、社員Ai と Bi のどちらが上司かは分かっていない。

社員 T が社長であり、それ以外の N-1 人全員が誰か 1 人の直属の部下であるとき、各社員の「階級」を求めるプログラムを作成してください。 
ただし、部下がいない社員の階級は 0 であり、部下がいる社員の階級は、直属の部下における階級の最大値に 
1 を足した値であるとします。

#--------------------------------#
深さ優先探索で最深部を保持する
"""
sys.stdin = io.StringIO(_INPUT)
import queue

N, T = map(int, input().split())
G = [[] for i in range(N + 1)]

# LISTで格納
for i in range(N - 1):
    A, B = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    #dprint(A, B)
    G[A].append(B)  # 0-index
    G[B].append(A)

H = [0 for i in range(N + 1)]


# 深さ優先探索
def dfs(G, H, cur, next) -> int:
    for n in G[next]:
        if n == cur:  # edgeが双方向のため
            continue
        height = dfs(G, H, next, n) + 1
        # 一番の深さを更新
        H[next] = max(H[next], height)
    return H[next]  #呼びもとに高さを返す


dfs(G, H, 0, T)
#print(H[1:])
print(*H[1:])
