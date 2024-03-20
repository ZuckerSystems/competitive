import io
import sys

_INPUT = """\
7
1 2 5 5 2 3 1
4
3 5
4 6
6 6
1 1
"""
sys.stdin = io.StringIO(_INPUT)
"""
3≤N≤100000
1≤D≤100000
1≤Ai≤100
2≤Li≤Ri≤N−1
"""
N = int(input())
A = list(map(int,input().split()))
D = int(input())
L = [ None ] * D
R = [ None ] * D

# 左右から見た最大の泊まれる人数のリストを作成しておく
# 工事している両隣の部屋のどちらか多い方が答えとなる
LmaxList = [ 0 ] * N
LmaxList[0] = A[0]
for i in range(1, N):
	# A[i]が左隣の人数よりも多い場合は更新
	LmaxList[i] = max(LmaxList[i - 1], A[i])

RmaxList = [ 0 ] * N
RmaxList[N-1] = A[N-1]
for i in reversed(range(0, N - 1)):
	# A[i]が右隣の人数よりも多い場合は更新
	RmaxList[i] = max(RmaxList[i + 1], A[i])
    
#print(LmaxList)
#print(RmaxList)

for i in range(D):
  L[i], R[i] = map(int,input().split())
  lmax = LmaxList[(L[i] -1) -1]
  rmax = RmaxList[(R[i] + 1) -1]
  print(max(lmax, rmax))
  
