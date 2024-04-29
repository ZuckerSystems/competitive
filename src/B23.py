import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
16
2 5
2 3
4 1
1 1
7 2
5 3
6 5
4 8
9 9
10 10
11 11
12 12
13 13
14 14
15 15
18 3
"""
sys.stdin = io.StringIO(_INPUT)
"""

"""
N = int(input())
X = [None] * N
Y = [None] * N

for i in range(0, N):
    X[i], Y[i] = map(int, input().split())

#print(points)


# 巡回セールスマン問題
# 厳密解法で 2^15計算
def calcDistance(x1, x2, y1, y2) -> float:
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


CONST_MAX_DISTANCE = 10000000

allDistanceList = [[0 for j in range(N)] for i in range(N)]


def all_distance(allDistanceList):
    # 全都市間を求めてしまう
    for i in range(N):
        for j in range(N):
            if i < j:
                distance = CONST_MAX_DISTANCE
                # デバッグのため精度を少し落とす場合はroundで丸める
                distance = calcDistance(X[i], X[j], Y[i], Y[j])
                #allGraph[i][j] = distance
                allDistanceList[i][j] = distance
                allDistanceList[j][i] = distance
    return allDistanceList


def get_distance(a, b, allDistanceList):
    return allDistanceList[a][b]


def all_patrol(n, allDistanceList):
    d = [[2**30 for b in range(2**n)] for i in range(n)]

    for i in range(n):
        d[i][2**i] = get_distance(0, i, allDistanceList)

    for b in range(2**n):
        for i in range(n):
            if b >> i & 1 == 0:
                continue
            for j in range(n):
                if b >> j & 1 == 1:
                    continue
                tmp = d[i][b] + get_distance(i, j, allDistanceList)
                if tmp < d[j][b | 2**j]:
                    d[j][b | 2**j] = tmp

    return d[0][2**n - 1]


# 処理開始
allDistanceList = all_distance(allDistanceList)
ans = all_patrol(N, allDistanceList)

print(ans)
