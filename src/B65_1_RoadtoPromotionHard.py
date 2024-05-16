import io
import sys

_INPUT = """\
15 1
1 2
2 3
1 4
1 5
1 6
6 7
2 8
6 9
9 10
10 11
6 12
12 13
13 14
12 15
"""
"""
株式会社 KYOPRO-MASTER には N (≤100000) 人の社員がおり、1 から N までの番号が付けられています。 
ライバル会社に勤務している太郎君は、以下の N-1 個の情報を入手しました。
i 個目の情報: 社員 Ai と社員 Bi は直属の上司と部下の関係にある。
ここで、社員Ai と Bi のどちらが上司かは分かっていない。

社員 T が社長であり、それ以外の N-1 人全員が誰か 1 人の直属の部下であるとき、各社員の「階級」を求めるプログラムを作成してください。 
ただし、部下がいない社員の階級は 0 であり、部下がいる社員の階級は、直属の部下における階級の最大値に 
1 を足した値であるとします。

#--------------------------------#
幅優先探索で自分の直属の部下の数を算出しながら根付き木を完成させる。
そこから部下算出関数で部下を算出 セグ木ぽいけどそのままでは無理

選択するアルゴリズム間違い。深さ優先探索で求めるべき
"""
sys.stdin = io.StringIO(_INPUT)
import queue

N, T = map(int, input().split())
graph = [[] for i in range(N + 1)]

# LISTで格納
for i in range(N - 1):
    A, B = map(int, input().split())
    #全ての経路を格納してgraphを作成する
    #dprint(A, B)
    graph[A].append(B)  # 0-index
    graph[B].append(A)

q = queue.Queue()
bossList = [0 for _ in range(N + 1)]  # 自分にとってのboss
nos = [0 for _ in range(N + 1)]  #部下の数
q.put((T, 0))
while not q.empty():
    sub, boss = q.get()
    bossList[sub] = boss  # ボスのNoを記録
    next = graph[sub]
    for n in next:
        if nos[n] == 0:

            nos[sub] += 1
            q.put((n, sub))

print(bossList)
print(nos)
