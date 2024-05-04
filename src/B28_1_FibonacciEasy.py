import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
10000000
"""
sys.stdin = io.StringIO(_INPUT)
"""
フィボナッチ数列の第 N 項aNを1000000007 (=10 9 +7) で割った余りを求めてください。
"""

N = int(input())

fibonacci = [0, 1, 1]

for i in range(3, N + 1):
    #print(i)
    fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % 1000000007)

fibonacciN = fibonacci[-1]
print(fibonacciN)
