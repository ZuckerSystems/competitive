import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
102 75
73 76
57 1
62 51
64 39
63 34
27 39
10 71
62 65
24 82
41 39
10 4
40 6
6 64
81 86
86 27
30 86
2 50
69 95
94 74
50 20
54 91
96 5
85 90
11 15
13 44
11 61
14 72
74 80
37 61
50 18
30 18
50 75
51 98
70 24
10 61
24 56
63 26
14 48
60 42
77 62
22 66
100 24
11 23
14 62
20 99
3 68
70 91
93 48
32 43
38 70
21 69
96 96
73 42
27 90
41 44
1 33
33 32
37 38
6 61
61 19
80 45
71 65
41 30
7 37
87 67
71 36
54 2
50 42
88 75
36 60
8 16
81 60
29 59
74 85
23 43
21 45
33 72
84 68
7 94
55 59
37 30
15 72
33 50
11 20
68 57
40 71
32 9
81 5
52 32
29 28
100 6
36 72
63 86
80 62
13 37
19 12
50 31
40 63
48 35
47 32
77 95
41 43
"""
# 題意がわかったので修正 全員がKの範囲に入っていることが条件
# わずか100msほどTLE 件数が増えてしかも組み合わせ可ばかりになるとループ再帰は無理かも
# AB値の範囲100✕100で探索したほうがよいかも
# しかしこの問題は終わりとする
sys.stdin = io.StringIO(_INPUT)

# 組み合わせ辞書を作る
# 組み合わを全探索する その間Kの範囲に全員参加できているか確認
# 既に参加した人を管理するLISTを用意
N, K = map(int, input().split())
AB = [[None] for i in range(N)]
for i in range(N):
    AB[i] = list(map(int, input().split()))

#print(AB)
# 全ての可能な組み合わせをN✕N  のループで作成
PearDict = dict()

for i in range(N):
    Pear = []
    iA = AB[i][0]
    iB = AB[i][1]
    for j in range(N):
        if i != j:
            jA = AB[j][0]
            jB = AB[j][1]
            if (iA + K >= jA or iA - K >= jA) and (iB + K >= jB
                                                   or iB - K >= jB):

                #if max(jA, iA) - min(jA, iA) <= K and max(jB, iB) - min(jB, iB) <= K:
                Pear.append(j)
            #print('j=', j)
    PearDict[i] = Pear
    #print(i)
#print(PearDict)
for me, partners in PearDict.items():
    print(me, len(partners))

answerCntList = [1] * N
dist = [-1] * N
# Amax Amin Bmax Bminを格納するリスト
KRange = [0, 101, 0, 101]


# K値が目標値に入っているか
def checkKRange(K, A, B) -> bool:
    return A >= KRange[0] and A <= KRange[1] and B >= KRange[
        2] and B <= KRange[3]


def changeKRange(K, A, B):
    # Amin
    if A - K > KRange[0]:
        KRange[0] = A - K
    # Amax
    if A + K < KRange[1]:
        KRange[1] = A + K
    # Bmin
    if B - K > KRange[2]:
        KRange[2] = B - K
    # Bmax
    if B + K < KRange[3]:
        KRange[3] = B + K
    #if KRange[3] == 91:
    #    print(91)


recursionCount = 0


def calcMaxPear(pearDict, me, partner, ans) -> int:
    global recursionCount

    ret = ans
    nextPear = pearDict.get(partner, [])
    for next in nextPear:
        # print('dist=', dist, 'next', next)
        if dist[next] != 1:
            if checkKRange(K, AB[next][0], AB[next][1]):
                recursionCount += 1
                ret = ret + 1  #次のメンバーとつながった
                dist[next] = 1
                changeKRange(K, AB[next][0], AB[next][1])

                # print('次のツリーへret', ret, 'me', me, 'next', next)
                return calcMaxPear(pearDict, partner, next, ret)

    # print('再帰後：', ret)
    return ret


# ペア表を走査し、全ての組み合わせを最初のペアにする

for me, partners in PearDict.items():
    #me = 0
    #partners = PearDict[0]
    # KRangeは一人目で初期化

    # print('--------------------------------', me)
    for partner in partners:
        # 最初のペアを決めたら初期化
        recursionCount = 0
        dist = [-1] * N
        dist[me] = 1
        dist[partner] = 1
        KRange = [0, 101, 0, 101]
        changeKRange(K, AB[me][0], AB[me][1])
        #print('start:', KRange)
        changeKRange(K, AB[partner][0], AB[partner][1])
        #print('second:', KRange)
        # パートナーと繋がれる人を探索(ツリーがどこまで続くのか不明なため再帰関数)
        # print('[初期のペア]', me, partner)
        answerCntList[me] = calcMaxPear(PearDict, me, partner, 2)
        #print('me', answerCntList[me])

print(recursionCount)
print(answerCntList)
print(len(answerCntList))
print(max(answerCntList))
"""
# 全ての組み合わせをループしながら算出
# ４重ループ 300✕300✕300✕300
for me, partners in PearDict.items():

    for partner in partners:
        answerCntList[me] = 2  # 最初のペア数を加算
        print(me, partner)
        for a, b in PearDict.items():
            if a == me:
                print('a-me=', a, me)
                continue

            # answerCntList[me] += 1  # 最初のペア数を加算
            for c in b:
                print('acb=', a, c, b)
                if c != partner:
                    # me partnerを除いたペア数を算出
                    answerCntList[me] += 1
            print('aend')
print(answerCntList)
print(max(answerCntList))
"""
