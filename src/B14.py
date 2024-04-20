import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
6 30
5 1 18 7 2 9
"""
"""
N 枚のカードがあり、i 枚目 (1≤i≤N) のカードには整数 Aiが書かれています。
カードの選び方は全部で2^N通りありますが、選んだカードの合計がちょうどKとなるようにする方法は存在しますか。

1≤N≤30
1≤K≤10^8
1≤Ai≤10^8

6 30
5 1 18 7 2 9
5+18+7=30 なので、Yes を出力してください。

2^10オーダにするためにリストを分割
全組み合わせはitertoolsで作成
"""
sys.stdin = io.StringIO(_INtdUT)

import bisect
import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

al = a[:(n // 2)]
ar = a[(n // 2):]
#print(al)
#print(ar)
#alの全組み合わせ
setAl = []
for i in range(1, len(al) + 1):
    for x in itertools.combinations(al, i):
        #print('x', x)
        if sum(x) == k:
            #print(x)
            print('Yes')
            exit(0)
        if sum(x) < k:
            setAl.append(sum(x))
#print(setAl)

setAr = []
#print(len(al))
for i in range(1, len(ar) + 1):
    for x in itertools.combinations(ar, i):
        #print('x', x)
        if sum(x) == k:
            #print(x)
            print('Yes')
            exit(0)
        if sum(x) < k:
            setAr.append(sum(x))
#print(setAr)
setAr.sort()
for i in range(0, len(setAl)):
    target = k - setAl[i]
    #print(target)
    idx = bisect.bisect_left(setAr, target)
    #print(idx, len(setAr))
    if idx < len(setAr):
        if setAr[idx] == target:
            print('Yes')
            exit(0)
print('No')
