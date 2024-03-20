
import io
import sys

_INPUT = """\
5
46 80 11 77 46
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# 解は配列内の順位を求めると算出できる
# 配列操作ライブラリ使用
import bisect
N = int(input())
A = list(map(int, input().split()))

# 重複削除してソートする（Aの破壊操作にならないように
Asort = sorted(list(set(A)))

# 解答はB
B = []

# idx値＝順位を求める
for a in A:
  idx = bisect.bisect_left(Asort, a)
  B.append(idx + 1)

print(*B)

