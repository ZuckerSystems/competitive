import io
import sys

_INPUT = """\
(())()
"""
"""
stack
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
import queue

S = input()

stack = queue.LifoQueue()
for i, s in enumerate(S):
    if s == '(':
        stack.put(i)
    if s == ')' and stack:
        print(stack.get() + 1, i + 1)
