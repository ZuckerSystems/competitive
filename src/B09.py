import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
13
667 637 1306 1293
69 957 768 1100
484 908 1452 1275
1427 38 1475 945
1475 1321 1500 1486
917 439 1002 1123
765 1231 1249 1307
376 263 1094 366
80 1194 239 1219
582 345 963 475
412 519 1275 617
1038 790 1464 1361
104 522 514 1354
"""
"""
13
667 637 1306 1293
69 957 768 1100
484 908 1452 1275
1427 38 1475 945
1475 1321 1500 1486
917 439 1002 1123
765 1231 1249 1307
376 263 1094 366
80 1194 239 1219
582 345 963 475
412 519 1275 617
1038 790 1464 1361
104 522 514 1354

1173461

二次元平面上に N 枚の紙があります．
それぞれの紙は，各辺が x 軸または y 軸に平行であるような長方形となっています． 
また、i 枚目の紙の左下座標は (Ai,Bi) であり，右上座標は (Ci,Di) です．
1 枚以上の紙が置かれている部分の面積を求めてください． 
なお入力される値はすべて整数です．
------------------------
d   ad         cd

b   ab         cb   

    a          c
------------------------
d   -1111111111+0 ここをゼロにしたいので
    111111111110
b   +1111111111- 

    a          c
下から累積和を取るのでcdは+にしてマイナスされるのを止める
------------------------
#累積和の問題
"""
sys.stdin = io.StringIO(_INtdUT)

import numpy as np

n = int(input())
matrix = np.zeros((1501, 1501), int)

for i in range(n):
    a, b, c, d = map(int, input().split())
    matrix[b][a] += 1
    matrix[d][a] -= 1
    matrix[b][c] -= 1
    matrix[d][c] += 1
#print(matrix)
matrixSum = np.cumsum(matrix, axis=0)
matrixSum = np.cumsum(matrixSum, axis=1)

#print(matrixSum)
print(np.count_nonzero(matrixSum >= 1))
