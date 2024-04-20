import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
4
10 30 40 20
"""
"""
N 個の足場があります。 
足場には 1,2,…,N と番号が振られています。 
各 i (1≤i≤N) について、足場 i の高さは h i です。
最初、足場 1 にカエルがいます。 
カエルは次の行動を何回か繰り返し、足場 N まで辿り着こうとしています。
足場 i にいるとき、足場 i+1 または i+2 へジャンプする。
このとき、ジャンプ先の足場を j とすると、コスト hi-h jlを支払う。
カエルが足場 N に辿り着くまでに支払うコストの総和の最小値を求めてください。
"""
sys.stdin = io.StringIO(_INtdUT)

n = int(input())
h = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[0] - h[1])
    else:
        #print('1個前から', dp[i - 1], abs(h[i - 1] - h[i]))
        #print('2個前から', dp[i - 2], abs(h[i - 2] - h[i]))

        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]),
                    dp[i - 2] + abs(h[i - 2] - h[i]))

#print(dp)
print(dp[n - 1])
