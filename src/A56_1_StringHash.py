import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
7 3
abcbabc
1 3 5 7
1 5 2 6
1 2 6 7
"""
sys.stdin = io.StringIO(_INPUT)
"""
substringした結果が同じかの判定問題
ハッシュ値計算するのが問題の名称からもわかるが
普通に作ってみる。もちろんTLE
"""

N, Q = map(int, input().split())
S = input()
Query = []

#f = open('A56-debug.txt', 'w', encoding='utf-8', newline='\n')
for i in range(Q):
    Query = list(map(int, input().split()))
    if S[Query[0] - 1:Query[1]] == S[Query[2] - 1:Query[3]]:
        #print('str', S[Query[0] - 1:Query[1]], S[Query[2] - 1:Query[3]])
        print('Yes')
        #f.write('Yes\n')
    else:
        print('No')
        #f.write('No\n')
#f.close()
