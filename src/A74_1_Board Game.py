import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
4
0 0 0 4
0 0 3 0
0 2 0 0
1 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)
"""
1
  2
    3
      4
        5
と並べる回数の問題。列と行の隣を交換　２次元バブルソート
"""

import numpy as np

n = int(input())
tmp = [[] for i in range(n)]
for i in range(n):
    tmp[i] = list(map(int, input().split()))

board = np.array(tmp)


def get_index(board, num):
    tmp = np.where(board == num)
    return (tmp[0][0], tmp[1][0])


sortTemp = [i for i in range(n)]
count = 0
for i in range(1, n + 1):
    pos = get_index(board, i)
    # 行の入替え

    for h in range(pos[0], i - 1, -1):
        so = sortTemp.copy()
        so[h] = h - 1
        so[h - 1] = h
        board = board[so, :]
        count += 1
        #print('h', board)

    for w in range(pos[1], i - 1, -1):
        so = sortTemp.copy()
        so[w] = w - 1
        so[w - 1] = w
        board = board[:, so]
        count += 1
        #print('w', board)

print(count)
