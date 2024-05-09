import io
import sys

_INPUT = """\
3
1 2 3
4 5 6
7 8 9
7
2 2 1
1 1 2
2 2 1
2 1 3
1 2 3
2 2 3
2 3 2
"""
"""
N×N のマス目があり、上から i 行目・左から j 列目のマス (i,j) には整数 A i,j​  が書かれています。以下の 2 種類の操作を処理するプログラムを作成してください。

交換操作：整数 x,y が与えられるので、x 行目と y 行目を交換する
取得操作：整数 x,y が与えられるので、マス (x,y) に書かれた整数を答える
交換操作の場合は 1 x y
取得操作の場合は 2 x y 

numpyの配列をそのまま入れ替えるとTLE
入替え表で実装
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
import numpy as np

N = int(input())
Amatrix = []
for i in range(N):
    A = list(map(int, input().split()))
    Amatrix.append(A)

Amatrix = np.array(Amatrix)
#print(Amatrix)

Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        idx1 = query[1]
        idx2 = query[2]
        swap = []
        for i in range(N):
            if i == idx1 - 1:
                swap.append(idx2 - 1)
            elif i == idx2 - 1:
                swap.append(idx1 - 1)
            else:
                swap.append(i)
        Amatrix = Amatrix[swap, :]
        #print(Amatrix)
    if query[0] == 2:
        print(Amatrix[query[1] - 1][query[2] - 1])
