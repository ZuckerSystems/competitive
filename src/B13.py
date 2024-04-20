import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
7 50
11 12 16 22 27 28 31
"""
"""
KYOPRO 商店には N 個の品物が売られており、i 番目の品物は Ai 円です。
連続する番号の品物を買う方法は全部で N(N+1)/2 通りありますが、
この中で合計価格が K 円以内となるような買い方は何通りでしょうか。

Aがソートされていればしゃくとり法が調子良さそうだが、条件にはないので普通にループ
"""
sys.stdin = io.StringIO(_INtdUT)

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
sum = 0
preSum = 0
mainIdx = 0
subIdx = 0

while mainIdx <= n - 1:
    #print(a[mainIdx])
    if a[mainIdx] <= k:
        ans += 1
        sum = a[mainIdx]
        subIdx = mainIdx + 1
        while subIdx <= n - 1:
            # print(a[subIdx])
            if sum + a[subIdx] <= k:
                ans += 1  #連続で買える限界まで買う
                sum += a[subIdx]
                subIdx += 1
            else:
                sum = 0
                break
    mainIdx += 1

print(ans)
