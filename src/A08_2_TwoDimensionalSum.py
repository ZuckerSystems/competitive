import io
import sys

_INPUT = """\
5 8
5 1 9 5 6 1 2 4
2 9 3 9 3 1 3 5
7 8 5 0 2 0 1 1
4 1 0 0 6 0 1 5
3 9 2 7 0 1 2 4
6
1 1 1 1
1 1 5 5
3 3 4 4
1 1 1 1
2 2 2 2
4 4 5 8
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import accumulate
class CumulativeSum:
  # 累積和演算クラス
  matrix = [] # マトリックス
  w = 0
  h = 0
  def __init__(self, h , w):
    # コンストラクタでは２次元配列数を指定
    self.matrix =  [ [ 0 ] * (w + 1) for i in range(h + 1) ]
    self.w = w + 1
    self.h = h + 1
  def setBesideArray(self, lst, h):
    self.matrix[h + 1] = [0] + list(accumulate(lst))
    #print(self.matrix[h]) # 先頭に0値を持つ累積和のリストを作成
  
  # 縦方向の累積和も算出
  def calcBVSum(self):
    for w in range(1 ,self.w):
        for h in range(1, self.h): # １行目は横方向と同じ値になるので
          self.matrix[h][w] = self.matrix[h - 1][w] + self.matrix[h][w]
    #print('-- 縦横累積和')
    #print(*self.matrix, sep='\n')
# 先頭に0要素を入れたmatrixを作成
# [0,  0,  0,  0,  0,   0,   0,   0,   0]
# [0,  5,  6, 15, 20,  26,  27,  29,  33]
# [0,  7, 17, 29, 43,  52,  54,  59,  68]
# [0, 14, 32, 49, 63,  74,  76,  82,  92]
# [0, 18, 37, 54, 68,  85,  87,  94, 109]
# [0, 21, 49, 68, 89, 106, 109, 118, 137]
  # 汎用性はないが指定された座標２点間の合計値を算出する TODO ここはmatrixを返して算出はクラス外で
  def getSumSquare(self, ha, wa, hb, wb):
    # 合計の初期化
    sum = self.matrix[hb][wb] 
    sum = sum + self.matrix[ha - 1][wa - 1] # マトリックス上２重に減算してしまう分を加算
    minusH = self.matrix[ha - 1][wb]
    minusW = self.matrix[hb][wa - 1]
    #print('sum=' + str(sum))
    #print('minusH=' + str(minusH))
    #print('minusW=' + str(minusW))
    return sum - minusH - minusW
  def printMatrix(self):
    #print(self.matrix)
    None

H, W = map(int, input().split())
X = [ None ] * H
cumulativeSum = CumulativeSum(H, W)
for h in range(H):
  cumulativeSum.setBesideArray(tuple(map(int,input().split())), h)

# 必要な累積和を算出しておく
cumulativeSum.calcBVSum()

Q = int(input())
ABCD = [ None ] * Q
for q in range(Q):
  ABCD[q] = list(map(int,input().split()))

# 出題数分ループ
for q in range(Q):
  a = ABCD[q][0]
  b = ABCD[q][1]
  c = ABCD[q][2]
  d = ABCD[q][3]  
  print(cumulativeSum.getSumSquare(a ,b, c, d))
