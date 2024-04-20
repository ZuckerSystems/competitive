import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
6
30 10 60 10 60 50
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
route = [0] * (n)
for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[0] - h[1])
        route[i] = 0
    else:
        #print('1個前から', dp[i - 1], abs(h[i - 1] - h[i]))
        #print('2個前から', dp[i - 2], abs(h[i - 2] - h[i]))
        pre1 = dp[i - 1] + abs(h[i - 1] - h[i])
        pre2 = dp[i - 2] + abs(h[i - 2] - h[i])
        dp[i] = min(pre1, pre2)
        #print(i)
        if pre1 < pre2:
            #print('-2', i)
            route[i] = i - 1
            #print(route)
        else:
            #print('-1', i - 1)
            route[i] = i - 2

#print(dp)
#print(dp[n - 1])

#print(route)

goal = n - 1
routemap = [n]
while goal > 0:
    routemap.append(route[goal] + 1)
    goal = route[goal]
    if goal == 0:
        break

print(len(routemap))
routemap.sort()
print(*routemap)
