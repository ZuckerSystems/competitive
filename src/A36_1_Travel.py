
import io
import sys

_INPUT = """\
9 10
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())

answer = (K - (N - 1) * 2) % 2
if answer == 1 or K - (N - 1) * 2 < 0:
    print('No')
else:
    print('Yes')
