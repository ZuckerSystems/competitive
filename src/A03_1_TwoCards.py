import io
import sys

_INPUT = """\
10 99
9 20 30 40 50 60 70 80 90 99
10 20 30 40 50 60 70 80 90 99
"""
sys.stdin = io.StringIO(_INPUT)

nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
ps = list(map(int, input().split()))
qs = set(list(map(int, input().split())))

result = 'No'
for p in ps:
    if (k - int(p)) in qs:
        result = 'Yes'
        break

print(result)
