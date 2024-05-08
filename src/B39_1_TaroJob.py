import io
import sys

_INPUT = """\
5 4
1 1
2 4
2 3
3 4
4 2
"""
"""
太郎君は今日から D 日間、仕事をしようと思いました。
仕事の選択肢は N 個あり、i 個目の仕事は Xi 日目以降になれば選ぶことができ、完了すれば Yi 円もらえます。
1つの仕事をするのに 1 日かかるとき、太郎君は最大何円を稼ぐことが出来ますか。

少しTLE numpyからの抽出が遅いのでdictに変更
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
import numpy as np
import heapq

N, D = map(int, input().split())

xy = [None] * N
moves = []
for i in range(N):
    xy[i] = list(map(int, input().split()))

npxy = np.array(xy)

#print(npxy)
queue = []
#heapq.heappush(queue, 0)
ans = 0
for i in range(1, D + 1):
    #next = heapq.heappop(queue)
    todayJob = npxy[(npxy[:, 0] == i)]
    #print(todayJob)
    for job in todayJob:
        # 今日始まるJOBをエンキュー-1をかけて最大値取得にする
        heapq.heappush(queue, (-1) * job[1])
    # １件デキュー
    if len(queue) > 0:
        ans += (-1) * heapq.heappop(queue)

print(ans)
