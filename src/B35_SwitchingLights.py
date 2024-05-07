import io
import sys

_INPUT = """\
7 3
1010111
"""
sys.stdin = io.StringIO(_INPUT)
"""
N 個の豆電球があり、i個目の豆電球はSi(S の i 文字目)が '1'のときON'0'のとき OFF になっています。
あなたは、以下の操作を何回でも行えます。

2 個の異なる豆電球を選び、ON/OFF の状態を反転させる。
ちょうどK個の豆電球が ON になっている状態にすることが可能であるかどうかを判定してください

ちょうどK個ではなく全部かと思っていたが修正 
"""
# nim=5
N, K = map(int, input().split())
S = [int(s) for s in input()]

countZero = S.count(0)
countOne = S.count(1)

#print(K, countOne, countZero)
#print(K - countOne)
if K == countOne:
    print('Yes')

elif K > countOne:
    #print(K, countOne)
    if (K - countOne) % 2 == 0 and K - countOne <= countZero:
        print('Yes')
    else:
        print('No')
elif K < countOne:
    if (K - countOne) % 2 == 0 and countOne - K <= countZero:
        print('Yes')
    else:
        print('No')
