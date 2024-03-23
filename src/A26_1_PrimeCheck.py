import io
import sys

_INPUT = """\
4
17
31
35
49
"""
sys.stdin = io.StringIO(_INPUT)

# ここから提出
# 試し割り法 上限はルート(num)+1まで
def isPrimeNumber(num):
    if num <= 3:
        return "Yes"
    for i in range(2, (int(num ** 0.5)) + 1):
        # print(num,i,num % i)
        if (num % i) == 0 :
            return "No"
    return "Yes"

# 入力
Q = int(input())
for i in range(0, Q):
    print(isPrimeNumber(int(input())))

