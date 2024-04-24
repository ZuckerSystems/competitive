import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
4 10
7 5 5 3
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

numpyを使うメリットがないのと、DPの逆算はでのカード取得ができないので方法変更
回答例を見ていて天才のアルゴリズムがあったので解析のみ
"""

sys.stdin = io.StringIO(_INtdUT)
N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

# 縦軸に求める数値
dp = [[None] * (N + 1) for _ in range(S + 1)]
# 初期値をセットしないとNoneがセットされ続ける
dp[0] = [[] for _ in range(N + 1)]

for i in range(1, S + 1):
    for j in range(1, N + 1):
        #print(i, j)
        if i < A[j]:
            #print('i<a')
            dp[i][j] = dp[i][j - 1]
        else:
            #print(i - A[j], [j - 1], dp[i - A[j]][j - 1])
            # 前の値と合計してi値になるかの判定。最終的にS値になる。
            if dp[i - A[j]][j - 1] == None:
                #print('None')
                dp[i][j] = dp[i][j - 1]
            else:
                #print('i値', i, 'j値', j)
                #print(dp[i - A[j]][j - 1])
                #print([A[j]])

                #if int(dp[i - A[j]][j - 1]) + int[A[j]] == i:
                dp[i][j] = dp[i - A[j]][j - 1] + [j]

#print(dp)
if dp[S][N] == None:
    print(-1)
else:
    print(len(dp[S][N]))
    print(*dp[S][N])
