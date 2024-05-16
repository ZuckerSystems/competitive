import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
15
1 2 1 1 1 6 2 6 9 10 6 12 13 12
"""
sys.stdin = io.StringIO(_INPUT)
"""
株式会社 KYOPRO-MASTER には N 人の社員がおり、地位順に 1 から N までの番号が付けられています。 
社長(社員 1)以外には直属の上司が 1 人おり、社員 i の直属の上司は社員 A i です。 各社員について、部下が何人いるかを出力してください。 ただし、社員 
y が社員 x の部下であるとは、x=y であり、なおかつ社員 y の直属の上司をたどって社員 x に到達できることを指します。
# まずはグラフを書いて愚直に実装
テストケース 00のみTLE
"""

import heapq

N = int(input())
A = list(map(int, input().split()))
graph = [list() for _ in range(N + 2)]


def countBuka(no) -> int:
    #print(no)
    cnt = -1
    queue = []
    heapq.heappush(queue, 0)
    for no in graph[no]:
        heapq.heappush(queue, no)
    #print('ループ前', queue)
    while queue:
        cnt += 1
        next = heapq.heappop(queue)
        #print(next)
        for no in graph[next]:
            heapq.heappush(queue, no)
    return cnt


for i in range(N - 1):
    graph[A[i]].append(i + 2)

#print(graph)

for i in range(1, N + 1):
    print(countBuka(i))
