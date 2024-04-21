import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
3 7
2 2 3
"""
"""
6
2 3 6 7 8 9

N 枚のカードがあり、i 枚目 (1≤i≤N) のカードには整数 Aiが書かれています。
カードの選び方は全部で2^N通りありますが、選んだカードの合計がちょうどKとなるようにする方法は存在しますか。
存在する場合はその方法を1 つ求めてください。
1≤N≤60
1≤K≤10000
1≤Ai≤10000

カードの中からいくつかを選んで、書かれた整数の合計が S となるようにする方法が存在する場合、選ぶカードの番号を 
P1 ,P2 ,…,Pk  として以下の形式で出力してください。
K
P1 P2 P3 P4 P5 P6

B14と同じ手法で、取得カードだけ後から再現する。
なぜかうまくいかない。
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
useValue = []
dictAl = dict()
isBreak = False
for i in range(1, len(al) + 1):
    for x in itertools.combinations(al, i):
        #print(idx)
        if sum(x) == k:
            #print(x)
            useValue += x
            isBreak = True
            break
        if sum(x) < k:
            dictAl[sum(x)] = x
    else:
        continue
    break
#print(dictAl)

dictAr = dict()
#print(len(al))
if not isBreak:
    for i in range(1, len(ar) + 1):
        for x in itertools.combinations(ar, i):
            #print('x', x)
            if sum(x) == k:
                #print(x)
                useValue += x
                isBreak = True
                break
            if sum(x) < k:
                dictAr[sum(x)] = x
        else:
            continue
        break
#print(dictAl)
#print(dictAr)
if not isBreak:
    lkeys = list(dictAl.keys())
    rkeys = list(dictAr.keys())

    #print(rkeys)
    for i in range(0, len(lkeys)):
        target = k - lkeys[i]
        #print(target)
        idx = bisect.bisect_left(rkeys, target)
        #print(idx, len(dictAr))
        if idx < len(rkeys):
            if rkeys[idx] == target:
                #print(rkeys[idx])
                #print(dictAr[rkeys[idx]])
                useValue += dictAl[lkeys[i]]
                useValue += dictAr[rkeys[idx]]
                isBreak = True
                break
if isBreak:
    #print(a)
    #print(useValue, sum(useValue))
    useCard = []
    for i in range(len(useValue)):

        idxl = bisect.bisect_left(a, useValue[i])
        idxr = bisect.bisect_right(a, useValue[i])
        #print('idxl', idxl)
        if (idxl + 1) in useCard:
            #print(idxl, a[idxl])
            for j in range(idxl, idxr):
                #print(j, a[j])
                if (j + 1) not in useCard:
                    useCard.append(j + 1)
                    break
        else:
            useCard.append(idxl + 1)
        #print('i', i, useCard)
    print(len(useCard))
    print(*useCard)
else:
    print('-1')
