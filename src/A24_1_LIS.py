import io
import sys

_INPUT = """\
6
6 2 1 7 8 9
"""
sys.stdin = io.StringIO(_INPUT)

# ここから提出
import bisect

# にぶたん DPは後ほどTODO
# 入力
N = input().split()
A = list(map(int, input().split()))

ans = []
for x in A:
    i = bisect.bisect_left(ans, x)
    if i == len(ans):
        ans.append(x)
    else:
        ans[i] = x
# 長さは連続した最後のLENで取れるが数字は置き換わっている
# print(ans)
print(len(ans))
