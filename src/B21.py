import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
7
abcdcba
"""
"""
問題文
太郎君は、長さ N の文字列 S に対して以下の操作を行うことで、回文を作りたいです。
S の中から（連続するとは限らない）文字を取り除く。残った文字を順番通りに連結する。
最長何文字の回文を作ることができるか、出力するプログラムを作成してください。

制約
1≤N≤1000
文字列 
S は英小文字からなる

"""

sys.stdin = io.StringIO(_INtdUT)
N = int(input())
S = input()
reversedS = S[::-1]

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if S[i - 1] == reversedS[j - 1]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

print(dp[-1][-1])
