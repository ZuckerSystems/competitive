import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
3
10 20 30
35 40 33
"""
sys.stdin = io.StringIO(_INPUT)
"""
あなたは夏休みの宿題 N 個を、毎日 1 つずつ終わらせなければなりません。宿題には 1 から N までの番号が付けられており、宿題i の 難易度 は整数 Aiで表されます。
また、夏休みi日目 (1≤i≤N) の気温は Bi度になることが予想されています。
「難易度x気温」の総和だけ労力がかかるとき、すべての宿題を終わらせるために必要な労力の最小値はいくつですか。

普通に解く
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

ans = 0
for i in range(n):
    ans += a[i] * b[i]

print(ans)
