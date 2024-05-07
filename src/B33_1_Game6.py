import io
import sys

_INPUT = """\
2 8 4
6 4
7 1
"""
"""
HxW のマス目に N 個のコマが置かれています。
i 個目のコマは上から Ai 行目、左から Bi 列目のマスに存在します。
太郎君と次郎君は交互に、「 1 つのコマを選んで左方向か上方向に 1 マス以上移動させる」という操作を行います。
同じ位置に複数のコマを置くことも許されます。
操作を行えなくなった方が負けであるとき、どちらが勝ちますか。

# 絶対にパズルゲーム作成以外で使い道ないが
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
N, H, W = map(int, input().split())

A = [None] * (N)
B = [None] * (N)
moves = []
for i in range(N):
    A[i], B[i] = map(int, input().split())
    if A[i] - 1 > 0:
        moves.append(A[i] - 1)
    if B[i] - 1 > 0:
        moves.append(B[i] - 1)
#print(moves)
nim = 0
for move in moves:
    nim = nim ^ move
    #print(nim)
if nim > 0:
    print('First')
else:
    print('Second')
