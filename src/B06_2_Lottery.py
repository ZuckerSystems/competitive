import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7
"""
"""
太郎君はくじをN 回引き， 回目の結果は A i でした.Ai=1 のときアタリAi=0 のときハズレを意味します． 
「L 回目から R 回目までの中では，アタリとハズレどちらが多いか？」という形式の質問が 
Q 個与えられるので， それぞれの質問に答えるプログラムを作成してください．

正答は累積和の引き算かと思うがギリギリ通ったのでOK
→累積和に修正 そんなに早くはならない
"""
sys.stdin = io.StringIO(_INtdUT)
import numpy as np

n = int(input())
a = np.array([0] + list(map(int, input().split())))
aSum = np.cumsum(a, dtype=np.int64)
q = int(input())
for i in range(q):

    l, r = map(int, input().split())
    hit = aSum[r] - aSum[l - 1]
    lose = r - l + 1 - hit
    if hit == lose:
        print('draw')
    elif hit > lose:
        print('win')
    else:
        print('lose')
