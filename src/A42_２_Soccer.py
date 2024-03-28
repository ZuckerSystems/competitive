import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
4 30
20 30
10 40
50 10
30 60
"""
# 題意がわかったので修正 全員がKの範囲に入っていることが条件
sys.stdin = io.StringIO(_INPUT)

# 組み合わせ辞書を作る
# 組み合わを全探索する その間Kの範囲に全員参加できているか確認
# 既に参加した人を管理するLISTを用意
N, K = map(int, input().split())
AB = [[None] for i in range(N)]
for i in range(N):
    AB[i] = list(map(int, input().split()))

#print(AB)
# 全ての可能な組み合わせをi-N 1+1-N  のループで作成
PearDict = dict()

for i in range(N):
    Pear = []
    iA = AB[i][0]
    iB = AB[i][1]
    for j in range(N):
        if i != j:
            jA = AB[j][0]
            jB = AB[j][1]

            if max(jA, iA) - min(jA, iA) <= K and max(jB, iB) - min(jB,
                                                                    iB) <= K:
                Pear.append(j)
            #print('j=', j)
    PearDict[i] = Pear
    #print(i)
print(PearDict)

answerCntList = [1] * N
dist = [-1] * N


def isPartnerAll(An, Bn) -> bool:
    listA = [An]
    listB = [Bn]
    for i in dist:
        if dist[i] == 1:
            listA.append(AB[i][0])
            listB.append(AB[i][1])
    print('maxlistA=', max(listA), K)
    print('maxlistA=', min(listA), K)
    print('maxlistB=', max(listB), K)
    print('maxlistB=', min(listB), K)
    print(max(listB))
    if (max(listA) - min(listA) < K) or (max(listB) - min(listB) < K):
        return False
    return True


def calcMaxPear(pearDict, me, partner, ans) -> int:
    ret = ans
    print('再帰前：', ret)
    dist[me] = 1
    dist[partner] = 1
    print('☆', dist, me, partner)
    print(me, partner)
    nextPear = pearDict.get(partner, [])
    print('nextPear', nextPear)
    for next in nextPear:
        print('dist=', dist, 'next', next)
        if dist[next] != 1:
            if isPartnerAll(AB[next][0], AB[next][1]):
                ret = ret + 1  #次のメンバーとつながった
                print('次のツリーへret', ret, 'me', me, 'next', next)
                return calcMaxPear(pearDict, partner, next, ret)

    #print('再帰後：', ret)
    return ret


for me, partners in PearDict.items():
    print('--------------------------------', me)
    for partner in partners:
        # dprint(me, partner)
        # パートナーと繋がれる人を探索(ツリーがどこまで続くのか不明なため再帰関数)
        dist = [-1] * N

        print('[初期のペア]', me, partner)
        answerCntList[me] = calcMaxPear(PearDict, me, partner, 2)
        #print('me', answerCntList[me])
print(answerCntList)
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
