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
   4
  3 3   3  
 2   2 2  
1     1  1
0123456789
----345438
index 4 では答えが1になるのではない。3が答え（いつ以来低値になっているが
Stackの最後をチェックして大きければ残すのみでいけそう
設問悪いね
"""

# 処理開始
N = int(input())
A = list(map(int, input().split()))

#print(*A)
stack = []
max = 0
ans = []
for i in range(N):
    if i == 0:
        ans.append(-1)
        continue

    if i >= 1:
        # 前日分をStackに入れてから処理開始
        stack.append([i - 1, A[i - 1]])
        cnt = len(stack)
        while cnt > 0:
            # 前日分が小さければ大きいものがあるまでPOP
            if stack[-1][1] <= A[i]:
                stack.pop()
                cnt -= 1
            else:
                break
    if len(stack) >= 1:
        # 最後のデータが大きいもの 何日ぶりの高値ではない気がするが
        ans.append(stack[-1][0] + 1)
    else:
        ans.append(-1)

print(*ans)
