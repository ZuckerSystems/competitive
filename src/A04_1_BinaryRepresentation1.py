import io
import sys

_INPUT = """\
1000
"""
sys.stdin = io.StringIO(_INPUT)

r = int(input())
# N=1000以下のため 2^9=512まで 2 4 8 16 32 64 128 256 512
# print('n=' + str(r))
cnt = 9
result = ''
while cnt > 0:
  q, r = divmod(r ,2 ** cnt)
  result = result + str(q)
  cnt -= 1
#最後の桁
result = result + str(r)
print(result)

