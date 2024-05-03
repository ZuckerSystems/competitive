import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)
"""
N1以下の素数をすべて求めよ

試し割り法で
1000000✕1000
1億回の除算計算ではある。
"""

N = int(input())


def is_prime_number(num):
    if num <= 3:
        return True
    for i in range(2, (int(num**0.5)) + 1):
        # print(num,i,num % i)
        if (num % i) == 0:
            return False
    return True


if N <= 3:
    print(N)
else:
    prime = True
    for i in range(2, N + 1):
        #print('i', i)
        r = N % i
        if is_prime_number(i):
            print(i)
