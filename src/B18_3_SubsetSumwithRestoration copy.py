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

全探索に近いかたちで
横軸に数を取る。縦軸はカード番号
"""

sys.stdin = io.StringIO(_INtdUT)

import numpy as np

# 入力
N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

# 縦にカード番号、横軸にS値のDP表を1-indexで作成する。
dp = np.zeros((N + 1, S + 1), int)
np.set_printoptions(threshold=(N + 1) * (S + 1))
for cardIdx in range(1, N + 1):
    print(cardIdx)
    for makeSum in range(1, S + 1):
        print(makeSum)
        #print(makeSum)
        # 現在のカードでその値が作れる
        if makeSum == A[cardIdx]:
            #print('作れる')
            dp[cardIdx][makeSum] = cardIdx

        # 前のカードとの合計で作れる
        if makeSum > A[cardIdx]:
            #print('前のカードとの合計で作れるかも')
            if dp[cardIdx - 1][makeSum - A[cardIdx]] > 0:
                #print('dp表の前の値＋現在値で作れる')
                dp[cardIdx][makeSum] = cardIdx
            else:
                # 前のカードまでで作れていたらそのIndexを引き継いでくる
                if dp[cardIdx - 1][makeSum] > 0:
                    dp[cardIdx][makeSum] = dp[cardIdx - 1][makeSum]
print(dp)

# cardsを逆算
cards = []
for i in range(1, N + 1):
    if dp[i][S] != 0:
        cards.append(dp[i][S])
        val = S - A[dp[i][S]]
        pos = i - 1
        while val > 0:
            cards.append(dp[pos][val])
            val -= A[dp[pos][val]]
            pos -= 1
            print(pos, val, cards)
            if val == 0:
                break
        else:
            continue
        break
if len(cards) == 0:
    print(-1)
else:
    print(*cards)
