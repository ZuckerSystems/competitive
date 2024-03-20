import io
import sys

_INPUT = """\
9 10
1 3 5 7 9 11 13 15 17
"""
sys.stdin = io.StringIO(_INPUT)

# 性能はギリギリTLE
# ここからが提出物
import itertools
from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 全組み合わせと差分リストを作成
diff = []
for pairs in list(itertools.combinations(A, 2)):
  #print(pairs)
  diff.append(pairs[1] - pairs[0])

# 差分リストのカウントを取ってK以下の合計を算出
# print(diff)
diffcount = Counter(diff)
count = 0
# K以下のリストだけに絞れればこの方法がよいかも
key = list(diffcount.keys())
for k in key:
  if k <= K:
    count = count + diffcount[k]

print(count)