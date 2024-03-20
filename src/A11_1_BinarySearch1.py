import io
import sys

_INPUT = """\
10 60
10 20 30 40 50 60 70 80 90 100
"""
sys.stdin = io.StringIO(_INPUT)

# 再帰のポインターつき２分探索
def binarysearch(lst, target, idx):
  # print(lst)
  p = len(lst) // 2
  if lst[p] == target:
    # print('point=' + str(idx) + ':p=' + str(p))
    return idx + p
  elif target < lst[p]:
    # print('point=' + str(idx) + ':p=' + str(p))
    return binarysearch(lst[:p], target, idx)
  elif target > lst[p]:
    # print('point=' + str(idx) + ':p=' + str(p))
    return binarysearch(lst[p+1:], target, idx + p + 1)

N, X = map(int, input().split())
A = list(map(int, input().split()))
result = binarysearch(A, X , 0)
print(result + 1)