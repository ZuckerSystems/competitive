import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
6
6 2 5 3 1 4
"""
sys.stdin = io.StringIO(_INPUT)
"""
株式会社 KYOPRO-MASTER は上場から 
N 日が経過しており、i 日目の株価は Ai円でした。太郎君は、それぞれの日について「株価が何日ぶりの高値を更新したか」を求めようと思いました。
ここでd 日目に対する 起算日 を次のように定義します。
i<d かつAi>Adを満たす最大のiただし、そのようなi が存在しない場合、起算日はないd=1,2,…,N について、起算日を計算してください。
[val,day] day降順ソート後にval昇順ソートしたものを用意 
[  1,  4]
[  2,  1]
[  3,  3]
[  4,  5]
[  6,  0]
reverse=True
allDistanceList.sort(key=lambda x: x[2])
"""


# ２次元一列目２分探索
def binarysearch(lst, target, idx):
    # print(lst)
    p = len(lst) // 2
    if lst[p][0] == target:
        # print('point=' + str(idx) + ':p=' + str(p))
        return idx + p
    elif target < lst[p][0]:
        # print('point=' + str(idx) + ':p=' + str(p))
        return binarysearch(lst[:p], target, idx)
    elif target > lst[p][0]:
        # print('point=' + str(idx) + ':p=' + str(p))
        return binarysearch(lst[p + 1:], target, idx + p + 1)


# 処理開始
N = int(input())
A = list(map(int, input().split()))

print(*A)
AValDay = []
max = 0
for i in range(N):
    AValDay.append([A[i], i])

AValDay.sort(key=lambda x: x[1], reverse=True)
AValDay.sort(key=lambda x: x[0])
for i in range(len(AValDay)):
    print(i, AValDay[i])

for i in range(N):
    if i == 0:
        print(-1)
        continue

    ret = binarysearch(AValDay, A[i], 0)
    print('day', i, 'ret', ret, AValDay[ret])
    noprint = True
    for j in range(ret, len(AValDay)):
        print('j', j, 'A[i]', A[i], '<AValDay[j][0]', AValDay[j][0], 'i', i,
              '>AValDay[j][1]', AValDay[j][1])
        if A[i] < AValDay[j][0] and i > AValDay[j][1]:
            # この条件ではNGでAValDay[ret]より下の配列の要素2の最大を求めればよいnumpyの仕様を確認中
            noprint = False
            print(AValDay[j][1] + 1)
            break
    # このループを抜けるのはこの時点で最大の場合
    if noprint:
        print(-1)
