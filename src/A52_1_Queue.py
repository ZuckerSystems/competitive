import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
5
1 taro
1 hanako
2
3
2
"""
sys.stdin = io.StringIO(_INPUT)
"""
先入れ先出しのqueueを実装する。
といっても標準listにその機能がある。また件数が多い場合はライブラリを利用する。
実務ではロギングや特定の処理だけデキューするシーンもあるのでライブラリを作成するか、探すか
スレッドセーフなのかも不明
"""
Q = int(input())
queue = []
for i in range(0, Q):
    Query = list(input().split())
    if Query[0] == '1':
        queue.append(Query[1])
    elif Query[0] == '2':
        print(queue[0])
    elif Query[0] == '3':
        queue.pop(0)
