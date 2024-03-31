import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
5 4
1 4 8
3 2
2
3 2
"""
sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
A = list(range(1, N + 1))  # Nまでのリスト
"""
変更操作：Query j = 1 x y のとき、Axの値を y に変更する
反転操作：Query j = 2 のとき、配列A を逆順にする
取得操作：Query j = 3 x のとき、Axの値を答える
"""
# reverse の繰り返しが遅いので、フラグでインデックスの読み替えに変更
Querys = [None] * Q
for i in range(Q):
    Querys[i] = list(map(int, input().split()))


def getIndex(index, isReversed, N):
    if not isReversed:
        return index
    else:
        #print(index, isReversed, N)
        return N - 1 - index


isReversed = False

for Query in Querys:
    if Query[0] == 1:
        A[getIndex(Query[1] - 1, isReversed, N)] = Query[2]
        #print(Query, A)
    elif Query[0] == 2:
        isReversed = not isReversed
        # A.reverse()
        #print(Query, A)
    elif Query[0] == 3:
        #print(getIndex(Query[1] - 1, isReversed, N), isReversed)
        print(A[getIndex(Query[1] - 1, isReversed, N)])
        #print(Query, A)
