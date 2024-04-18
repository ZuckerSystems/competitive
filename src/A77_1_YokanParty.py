import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954
"""
sys.stdin = io.StringIO(_INtdUT)
"""
左右の長さが L [cm] のようかんがあります。 N 個の切れ目が付けられており、左から i 番目の切れ目は左から A i
  [cm] の位置にあります。

あなたは N 個の切れ目のうち K 個を選び、ようかんを K+1 個のピースに分割したいです。そこで、以下の値を スコア とします。
K+1 個のピースのうち、最も短いものの長さ（cm 単位）スコアが最大となるように分割する場合に得られるスコアを求めてください。

おそらく正答はセグメント木だと思うが区間検索のアルゴリズムが難しいので
numpy.diffでおおよそのバケット分割で検討する。
"""

n, l = map(int, input().split())
k = int(input())
a = [0] + list(map(int, input().split()))
a.append(l)

import numpy as np

npa = np.array(a, dtype=np.int64)
npaDiff = np.diff(npa)
print(npa)
print(npaDiff)

#目標値
targetValue = l // (k + 1)
print(targetValue)
buckets = []
bucket = []
length = 0
cut = 0
for i in range(n + 1):
    if cut < k:
        length += npaDiff[i]
        bucket.append(npaDiff[i])
        if length + npaDiff[i + 1] >= targetValue:
            buckets.append(bucket.copy())
            bucket.clear()
            cut += 1
            length = 0
    else:
        bucket.append(npaDiff[i])

buckets.append(bucket)
print(buckets)

for i in range(len(buckets)):
    print(sum(buckets[i]))
