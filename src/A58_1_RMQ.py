import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
8 4
1 3 16
2 4 7
1 5 13
2 4 7
"""
sys.stdin = io.StringIO(_INPUT)
"""
長さ N の数列A=(A1 ,A2 ,…,AN) があり、最初はすべての要素が 
0 になっています。以下の 2 種類のクエリを処理してください。
クエリ 1：Apos  の値をx に更新する。
クエリ 2：Al ,Al+1 ,…,Ar−1の最大値を答える。
セグメント木で解くのだと思うが愚直にといてみる。
→当然のTLE
"""
N, Q = map(int, input().split())

lst = [0] * (N + 1)

for i in range(Q):
    query = list(map(int, input().split()))
    # 0index開始なのでQueryの数字-1から取得する必要がある
    if query[0] == 1:
        lst[query[1]] = query[2]
    elif query[0] == 2:
        print(max(lst[query[1]:query[2]]))
