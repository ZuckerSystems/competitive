import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
4 4 3
...#
..#.
.#..
.###
"""
sys.stdin = io.StringIO(_INPUT)
"""
縦 H 行、横 W 列のマス目があります。上から i 行目・左から j 列目のマス (i,j) の色は c i,j であり、c i,j  = . のとき白色、 c i,j = # のとき黒色で塗られています。
あなたは「ある行またはある列を選び、すべて黒で塗り替える」という操作を K 回まで行うことができます。最大で何個のマスを黒くすることができますか。
普通に解く
"""
h, w, k = map(int, input().split())
import numpy as np

tmp = [None] * h
for i in range(h):
    str = input()
    str = str.replace('#', '1')
    str = str.replace('.', '0')

    #print(str)
    tmp[i] = list(map(int, list(str)))  #str.split()では先頭のゼロが消える
    #print(tmp[i])

board = np.asarray(tmp)


def min_sum(board, h, w):
    # 行
    verticalSum = np.sum(board, axis=0)
    #print('verticalSum', verticalSum)
    # 列
    horizontalSum = np.sum(board, axis=1)
    #print('horizontalSum', horizontalSum)
    maxIndex = 0
    axis = 0
    vmin = np.argmin(verticalSum)
    hmin = np.argmin(horizontalSum)
    #print(h - verticalSum[vmin], w - horizontalSum[hmin])
    if (h - verticalSum[vmin]) <= (w - horizontalSum[hmin]):
        axis = 0
        maxIndex = hmin
    else:
        axis = 1
        maxIndex = vmin
    return (axis, maxIndex)


def line_change_value(h, w, k):
    if k < h and k < w:
        # 行だけ消した最大
        verticalSum = np.sum(board, axis=0)
        #print(verticalSum)
        verticalSum = np.sort(verticalSum)[::-1]
        #print(verticalSum, h - k)
        varrivalMax = verticalSum[0:h - k]
        #print('varrivalMax', varrivalMax)
        # 列だけ消した最大
        horizontalSum = np.sum(board, axis=1)
        horizontalSum = np.sort(horizontalSum)[::-1]
        #print(horizontalSum, w - k)
        horizonMax = horizontalSum[0:w - k]
        #print('horizonMax', horizonMax)
        #print(h, w, k)
        return max(np.sum(varrivalMax) + w * k, np.sum(horizonMax) + h * k)
    return 0


#print(board)
# 行だけ列だけ消して最大になる場合の考慮
preliminary = line_change_value(h, w, k)

#print('暫定値', preliminary)
for i in range(k):
    axis, minIndex = min_sum(board, h, w)
    #print(axis, minIndex)
    if axis == 0:
        for i in range(w):
            board[minIndex, i] = 1
    elif axis == 1:
        for i in range(h):
            board[i, minIndex] = 1
    #print(board)
#print(board)
print(max(board.sum(), preliminary))
