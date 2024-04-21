import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
10 100
14 23 18 7 11 23 23 5 8 2
"""
"""
10 100
14 23 18 7 11 23 23 5 8 2

3 7
2 2 3

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

丁寧に作ったがTLE3/21
aの数が減っているので全幅探索したほうが早いかも
"""

sys.stdin = io.StringIO(_INtdUT)

import bisect
import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = (n // 2)
al = a[:mod]
ar = a[mod:]


def getIndexAndCards(indexAndCard, addIndex):
    index = []
    cards = []
    sums = 0
    for x in indexAndCard:
        index.append(x[0])
        cards.append(x[1])
        sums += x[1]
    return [[sums], [x + addIndex for x in index], list(cards)]


# 見つかった場合の応答
def printAnswer(cards):
    print(len(cards))
    print(*[x + 1 for x in cards])
    exit(0)


#print(al)
#print(ar)
useCard = []
#alの全組み合わせ
alMatrix = []
isBreak = False
for i in range(1, len(al) + 1):
    for x in itertools.combinations(enumerate(al), i):
        ret = getIndexAndCards(x, 0)
        #print(ret)
        if ret[0][0] == k:
            printAnswer(ret[1])
        alMatrix.append(ret)

#print(alMatrix)

arMatrix = []
for i in range(1, len(ar) + 1):
    for x in itertools.combinations(enumerate(ar), i):
        ret = getIndexAndCards(x, mod)
        if ret[0][0] == k:
            #print(ret)
            printAnswer(ret[1])
        arMatrix.append(ret)

#for x in arMatrix:
#    print(x)

arMatrix.sort(key=lambda x: x[0])
#print('---------------------------------------------')
#cnt = 0
#for x in arMatrix:
#print(x)
#cnt += 1
#print('len ar', len(arMatrix), cnt)

#print('---------------------------------------------')
#for x in alMatrix:
#    print(x)

for l in alMatrix:
    target = k - l[0][0]
    #print('ターゲット:L現在値:', target, l[0][0])

    left = 0
    right = len(arMatrix) - 1
    mid = (left + right) // 2
    #print(left, mid, right)
    while left <= right:
        midValue = arMatrix[mid][0][0]
        #print('にぶたん', target, midValue, l[0][0])
        if midValue == target:
            #見つかった場合の処理
            #print('発見')
            #print(l[1], arMatrix[mid][1])
            useCard = l[1] + arMatrix[mid][1]
            #print(alMatrix[i][1])
            #print(useCard)

            printAnswer(useCard)
            break
        elif midValue < target:
            left = mid + 1
            mid = (left + right) // 2
            continue
        elif midValue > target:
            right = mid - 1
            mid = (left + right) // 2
            continue

print('-1')
