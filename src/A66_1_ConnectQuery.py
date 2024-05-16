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
クエリ 1:頂点 u と頂点 v を双方向に結ぶ辺を追加する。
クエリ 2:頂点 u と頂点 v は同じ連結成分に属するかを答える。
ただし、最初はグラフに辺が一本もなく、与えられるクエリの数は Q 個であるとします。

ショートコードで汚いが
→5/12 TLE
"""

n, q = map(int, input().split())
g = []


def sg(u, v, g: list):
    uv = {u, v}
    for i in g:
        if not i.isdisjoint(uv):
            i.update(uv)
            return
    #print('add', uv)
    g.append(uv)


for i in range(q):
    qy, u, v = map(int, input().split())
    if qy == 1:
        sg(u, v, g)
    else:
        uv = {u, v}
        ret = False
        for i in g:
            #print(i, uv)
            if i >= uv:
                print('Yes')
                ret = True
                break
        if not ret:
            print('No')
