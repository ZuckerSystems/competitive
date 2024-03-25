
import io
import sys

_INPUT = """\
3
3 5 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

# ニムゲーム計算
# https://www.forcia.com/blog/002362.html
