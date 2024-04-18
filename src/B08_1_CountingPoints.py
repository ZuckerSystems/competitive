import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
5
1 3
2 5
3 4
2 6
3 3
3
1 3 3 6
1 5 2 6
1 3 3 5
"""
"""
二次元平面上に N 個の点があります.i 個目の点の座標は (Xi,Yi) です．
 「x 座標が a 以上 c 以下であり，座標が b 以上 d 以下であるような点は何個あるか？」
 という形式の質問が Q 個与えられるので，それぞれの質問に答えるプログラムを実装してください．
 なお，入力される値はすべて整数です．

 import numpy as np

n = int(input())
matrix = np.zeros((1501, 1501), int)

for i in range(n):
    x, y = map(int, input().split())
    matrix[x][y] += 1

#print(matrix)
matrixSum = np.cumsum(matrix, axis=0)
matrixSum = np.cumsum(matrixSum, axis=1)
#print(matrixSum)

q = int(input())
for i in range(q):
    a, b, c, d = map(int, input().split())
    #print(a, b, c, d)
    p1 = matrixSum[a - 1, b - 1]
    p2 = matrixSum[c, b - 1]
    p3 = matrixSum[a - 1, d]
    p4 = matrixSum[c, d]
    #matrixSum[a - 1, b - 1] = 98
    #matrixSum[c, b - 1] = 99
    #matrixSum[a - 1, d] = 100
    #matrixSum[c, d] = 101

    print(p4 - p3 - p2 + p1)
1844 msでギリギリAC。numpy遅いのか。
"""

sys.stdin = io.StringIO(_INtdUT)
import numpy as np

n = int(input())
matrix = np.zeros((1501, 1501), int)

for i in range(n):
    x, y = map(int, input().split())
    matrix[x][y] += 1

#print(matrix)
matrixSum = np.cumsum(matrix, axis=0)
matrixSum = np.cumsum(matrixSum, axis=1)
#print(matrixSum)

q = int(input())
for i in range(q):
    a, b, c, d = map(int, input().split())
    #print(a, b, c, d)
    p1 = matrixSum[a - 1, b - 1]
    p2 = matrixSum[c, b - 1]
    p3 = matrixSum[a - 1, d]
    p4 = matrixSum[c, d]
    #matrixSum[a - 1, b - 1] = 98
    #matrixSum[c, b - 1] = 99
    #matrixSum[a - 1, d] = 100
    #matrixSum[c, d] = 101

    print(p4 - p3 - p2 + p1)
