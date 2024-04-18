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
"""
sys.stdin = io.StringIO(_INtdUT)
import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
q = int(input())
#print(a)
for i in range(q):

    l, r = map(int, input().split())
    hit = np.sum(a[l - 1:r])
    lose = r - l + 1 - hit
    if hit == lose:
        print('draw')
    elif hit > lose:
        print('win')
    else:
        print('lose')
