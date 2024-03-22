import io
import sys

_INPUT = """\
10 10
10 20 30 40 50 60 70 80 90 99
"""
sys.stdin = io.StringIO(_INPUT)

n = list(map(int, input().split()))[1]
xs = set(list(map(int, input().split())))

if n in xs:
    print('Yes')
else:
    print('No')
