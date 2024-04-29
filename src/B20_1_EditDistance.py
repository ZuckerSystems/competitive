import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
ab
azb
"""
"""
文字列 S と T が与えられます。
あなたは、文字列 S に対して以下の 3 種類の操作を行うことができます。

操作1：S 中の文字を 1 つ選び、削除する。
操作2：S 中の文字を 1 つ選び、別の文字に変更する。
操作3：S 中の適当な位置に、文字を 1 つ挿入する。

最小何回の操作で、文字列 S を T に一致させることができますか。

S の文字数は 1 以上 2000 以下
T の文字数は 1 以上 2000 以下
S,T は英小文字からなる

・部分一致している連続部分はそのまま利用する。
・1文字不足一致は変更。1回の操作で3文字 betweenIns
"""

sys.stdin = io.StringIO(_INtdUT)

S = input()
T = input()

dp = [[0 for _ in range(len(S) + 1)] for _ in range(len(T) + 1)]

for i in range(len(dp)):
    dp[i][0] = i
    for j in range(len(dp[i])):
        if i == 0:
            dp[i][j] = j
        elif j > 0:
            # １文字前が一致している場合コスト０
            if T[i - 1] == S[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 一文字前が一致指定な場合コスト１
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1

            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)

print(dp[-1][-1])
