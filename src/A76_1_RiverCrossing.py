import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
5 65 7 37
5 15 30 50 55
"""
sys.stdin = io.StringIO(_INtdUT)
"""
川幅がW メートルである KYOPRO 川には、 N 個の足場が一直線上に並べられており、
西から順に 1 から N までの番号が付けられています。足場 i (1≤i≤N) は西岸から X i​  メートルの位置にあります。
太郎君は東方向のジャンプを繰り返すことで、西岸から東岸まで移動しようと思いました。
しかし、一回のジャンプで飛ぶ距離は長すぎても短すぎてもダメであり、 
L メートル以上 R メートル以下でなければなりません。移動方法は全部で何通りありますか。

解法）
石をノードに見立てて各ノードまでのルート数を算出しながらゴールする配るDPで
TLE N値が最大150,000✕150,000のループ処理になるため
"""

n, w, l, r = map(int, input().split())
x = list(map(int, input().split()))

# スタート、ゴール地点もxに追加
x.append(w)
x.insert(0, 0)
dp = [0] * (n + 2)
dp[0] = 1
for i in range(n + 2):
    routeCount = dp[i]
    for j in range(i + 1, n + 2):
        #print(x[j] - x[i], l, r)
        if x[j] - x[i] >= l:
            if x[j] - x[i] <= r:
                dp[j] += routeCount
            else:
                break

#print(dp)
print(dp[n + 1])
