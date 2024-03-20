import io
import sys

# list_transposed = [list(x) for x in zip(*list_org)]


_INPUT = """\
5 5 2
1 1 3 3
2 2 4 4
"""
sys.stdin = io.StringIO(_INPUT)

# 加算・減算ポイントの座標を作成し横縦の累積和を算出して雪の高さを求める。
# 横縦の累積和を取ると、減算し過ぎのポイントがあるのでそこは加算する

# ここから提出
from itertools import accumulate
class CumulativeSum:
  # 累積和演算クラス
  matrix = [] # マトリックス
  sum_matrix_baseline = []
  sum_matrix_all = []
  h = 0
  w = 0
  def __init__(self, lst, h , w):
    # コンストラクタでは２次元配列数を指定
    self.matrix = lst
    self.sum_matrix_baseline = [ [ 0 ] * (w) for i in range(h) ] # もらったリストから作成したいが手抜き
    self.sum_matrix_all = [ [ 0 ] * (w) for i in range(h) ] # もらったリストから作成したいが手抜き
    self.h = h
    self.w = w
  # 横方向の累積和
  def calcBesideSum(self):
    for i in range(len(self.matrix) - 1):
      self.sum_matrix_baseline[i] = list(accumulate(self.matrix[i]))
      # print(self.sum_matrix_baseline[i]) # 先頭に0値を持つ累積和のリストを作成

  # 縦方向の累積和 list_transposed = [list(x) for x in zip(*list_org)]
  def calcVerticalSum(self):
    # 縦横を入れ替え
    temp = [list(x) for x in zip(*self.sum_matrix_baseline)]
    temp2 = [ [ 0 ] * (self.h) for i in range(self.w) ]
    # 論理和
    for i in range(len(temp)):
      temp2[i] = list(accumulate(temp[i]))
    # もう一度縦横を入れ替え
    self.sum_matrix_all = [list(x) for x in zip(*temp2)]
    # print('縦累積和')
    # print(*self.sum_matrix_all, sep='\n') # 縦方向も累積和
  # 算出した累積和を参照させる
  def getMatrixAllSum(self):
    return self.sum_matrix_all
  def printMatrix(self):
    #print(self.matrix)
    None


H, W, N = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
C = [ None ] * N
D = [ None ] * N
X = [ None ] * (W)
for t in range(N):
  A[t], B[t], C[t], D[t] = map(int, input().split())

# 地図Ｗ✕Ｈを作成
matrix = [ [ 0 ] * (W + 2) for i in range(H + 2) ]
# 加算減算の座標を指定
for t in range(N):
    matrix[A[t]][B[t]] += 1
    matrix[A[t]][D[t]+1] -= 1 #横方向の減算ポイント
    matrix[C[t]+1][B[t]] -= 1 #縦方向の減算ポイント
    matrix[C[t]+1][D[t]+1] += 1 #縦横２回減算するので止める

# 累積和演算にデータを渡す
cumulativeSum = CumulativeSum(matrix, H + 2 , W + 2)
cumulativeSum.calcBesideSum()
cumulativeSum.calcVerticalSum()

result = cumulativeSum.getMatrixAllSum()
for h in range(1, H + 1):
  print(' '.join(map(str, result[h][1: W + 1])))