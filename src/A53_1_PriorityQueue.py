import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
10
1 914575
3
1 648772
3
1 190629
1 47202
1 894325
1 804784
3
2
"""
sys.stdin = io.StringIO(_INPUT)
"""
優先順位付きのキュー
"""
import heapq

Q = int(input())
priorityQueue = []
heapq.heapify(priorityQueue)
for i in range(0, Q):
    #print(i, priorityQueue)
    Query = list(input().split())
    if Query[0] == '1':
        heapq.heappush(priorityQueue, int(Query[1]))
    elif Query[0] == '2':
        print(priorityQueue[0])
    elif Query[0] == '3':
        heapq.heappop(priorityQueue)
        #print(i, priorityQueue)
