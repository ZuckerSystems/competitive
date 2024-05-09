import io
import sys

_INPUT = """\
4 6
1 4 1 4 2 1
"""
"""
N 人の生徒がクイズ大会に参加しました。
この大会では M 問が出題され、i 問目では Ai 番目の生徒を除く全員が正解しました。
各生徒の最終的な正解数を求めるプログラムを作成してください。

簡単な問題
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など

N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] + [M] * N

for a in A:
    ans[a] -= 1

for i in range(1, N + 1):
    print(ans[i])
