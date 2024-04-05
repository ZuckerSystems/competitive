import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
6 6
1 4
2 3
3 4
5 6
1 2
2 4
"""
sys.stdin = io.StringIO(_INPUT)
"""
もしグラフ全体が連結であれば、 The graph is connected. と出力する
そうでなければ、 The graph is not connected. と出力する
"""
# 愚直に問いてみる
N, M = map(int, input().split())

WOODS = [list() for j in range(N + 1)]
index = 0
for i in range(M):
    A, B = map(int, input().split())
    if i == 0:
        WOODS[0].append(A)
        WOODS[0].append(B)
    else:
        tmp = [A, B]
        # print('処理対象', tmp)
        flg = False
        for j in range(index + 1):
            # print('j', j, A, B)
            #共通の要素を持たない
            #print(use_index, WOODS, i, tmp)

            if not set(WOODS[index]).isdisjoint(tmp):
                # 共通の要素を持つのでまとめて終了
                # print('結合処理', WOODS[j], tmp)
                if A not in WOODS[j]:
                    # print('A append')
                    WOODS[j].append(A)
                if B not in WOODS[j]:
                    # print('B append')
                    WOODS[j].append(B)
                flg = True
                break
        if flg == False:
            # 共通の要素をどのグラフとも持たない
            # print('新規作成', index)
            index += 1
            WOODS[index].append(A)
            WOODS[index].append(B)
            #print(index, WOODS)

# print('結合前', WOODS)

if index >= 1:
    flg = True
    while flg:
        flg = False
        for i in range(1, index + 1):
            # print(index, WOODS[0], WOODS[i],
            #      set(WOODS[0]).isdisjoint(WOODS[i]), False)
            if not set(WOODS[0]).isdisjoint(WOODS[i]):
                # print('合体')
                WOODS[0] = WOODS[0] + WOODS[i]
                WOODS[i] = []
                flg = True
if len(WOODS[0]) == N:
    print('The graph is connected.')
else:
    print('The graph is not connected.')
