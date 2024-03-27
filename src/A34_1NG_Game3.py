
import io
import sys

_INPUT = """\
2 2 3
5 8
"""
sys.stdin = io.StringIO(_INPUT)

# ニムゲーム計算
# https://www.forcia.com/blog/002362.html

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

grundy = []

# NG遅い。バグがある。
# numの数が取り得るGrundy値をlistで返却 canTakenNo1 < canTakenNo2 で呼び出す
# 再帰

# このやり方だと、同じ石の数のGrundy数を何回も求めてしまう


def calcGrundy(num, canTakenNo1, canTakenNo2, grundyList) -> list:
    # print(num, canTakenNo1, canTakenNo2, grundyList)
    if num >= canTakenNo2:
        # print('canTakenNo2')
        grundyList.append(2)
        calcGrundy(num - canTakenNo2, canTakenNo1, canTakenNo2, grundyList)

    if num >= canTakenNo1:
        # print('canTakenNo1')
        grundyList.append(1)
        calcGrundy(num - canTakenNo1, canTakenNo1, canTakenNo2, grundyList)

    if num < canTakenNo1:
        grundyList.append(0)
        # print('最後', grundyList)
        return grundyList

    else:
        return grundyList


grundy = calcGrundy(A[0], X, Y, grundy)
# print(grundy)

nim = grundy[0]
for i in range(1, len(grundy)):
    nim = nim ^ grundy[i]

if nim == 0:
    print('Second')
else:
    print('First')
