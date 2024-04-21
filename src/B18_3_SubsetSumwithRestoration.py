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

全探索に近いかたちで
横軸に数を取る。縦軸はカード番号
"""

sys.stdin = io.StringIO(_INtdUT)

# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 動的計画法（i=0）
dp = [[None] * (S + 1) for i in range(N + 1)]
dp[0][0] = True
for i in range(1, S + 1):
    dp[0][i] = False

# 動的計画法（i=1）
for i in range(1, N + 1):
    for j in range(0, S + 1):
        # 今までのカードで作ったDP表を引き継ぐ
        if j < A[i - 1]:
            if dp[i - 1][j]:
                # 今までのカードで作れているので今回の取捨によらず作れる
                dp[i][j] = True
            else:
                dp[i][j] = False

        if j >= A[i - 1]:
            if dp[i - 1][j] == True or dp[i - 1][j - A[i - 1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

# 動的計画法の復元
if dp[N][S] == False:
    print(-1)
else:
    pos = S
    count = []
    for j in range(N - 1, -1, -1):
        if dp[j][pos] == False:
            count.append(j + 1)
            pos -= A[j]
    #出力
    count.sort()
    print(len(count))
    print(*count)
