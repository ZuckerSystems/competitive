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
まずは愚直に作ってみる
→4/15のTLE
"""
# 処理開始
N = int(input())
A = list(map(int, input().split()))

Astack = []  #stackとしては使わないが
max = 0
for i in range(N):
    if i == 0:
        print(-1)
        max = A[i]
        Astack.append([i, A[i], max])
    else:
        #print(i, max)
        if max <= A[i]:
            max = A[i]
            print(-1)
            Astack.append([i, A[i], max])
        else:
            for j in range(i - 1, -1, -1):
                # 一つ前の値を逆上る
                #print('J上り中', j, Astack[j][1], A[i])
                if Astack[j][1] > A[i]:
                    print(j + 1)
                    break

            Astack.append([i, A[i], max])
    #print(Astack)
