import io
import sys

_INPUT = """\
2
8 16
32 64
3
2 2 1
1 1 2
2 2 1
"""
"""
N×N のマス目があり、上から i 行目・左から j 列目のマス (i,j) には整数 A i,j​  が書かれています。以下の 2 種類の操作を処理するプログラムを作成してください。

交換操作：整数 x,y が与えられるので、x 行目と y 行目を交換する
取得操作：整数 x,y が与えられるので、マス (x,y) に書かれた整数を答える
交換操作の場合は 1 x y
取得操作の場合は 2 x y 

入替え表で実装 1-indexに合わせて修正
またもやTLE
numpyが意味がなくなっていたので削除してAC
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
N = int(input())
Amatrix = [[0] * (N + 1)]

for i in range(N):
    A = [0] + list(map(int, input().split()))
    Amatrix.append(A)

idxMap = [_ for _ in range(N + 1)]

Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        #print('query1', query)
        idxMap[query[1]], idxMap[query[2]] = idxMap[query[2]], idxMap[query[1]]
        #print('idxMap', idxMap)
    if query[0] == 2:
        print(Amatrix[idxMap[query[1]]][query[2]])
