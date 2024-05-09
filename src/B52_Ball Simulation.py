import io
import sys

_INPUT = """\
100 50
....................................................................................................
"""
"""
出題の意味はよく理解できないがとりあえずそのまま実装してみる。
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
import queue

N, X = map(int, input().split())
a = [None] + list(input())  # 1-index

stack = queue.LifoQueue()

stack.put(X)
a[X] = '@'

while not stack.empty():
    p = stack.get()
    if a[p - 1] == '.':
        a[p - 1] = '@'
        if p - 1 > 0:
            stack.put(p - 1)
    if a[p + 1] == '.':
        a[p + 1] = '@'
        if p + 1 < N:
            stack.put(p + 1)

print(''.join(a[1:]))
