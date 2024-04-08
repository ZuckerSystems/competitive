import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
15
1 2 1 1 1 6 2 6 9 10 6 12 13 12
"""
sys.stdin = io.StringIO(_INPUT)
"""
株式会社 KYOPRO-MASTER には N 人の社員がおり、地位順に 1 から N までの番号が付けられています。 
社長(社員 1)以外には直属の上司が 1 人おり、社員 i の直属の上司は社員 A i​  です。 各社員について、部下が何人いるかを出力してください。 ただし、社員 
y が社員 x の部下であるとは、x=y であり、なおかつ社員 y の直属の上司をたどって社員 x に到達できることを指します。
# まずはグラフを書いて愚直に実装
Aをリバースしながら加算していくだけかな。なるべくショートコードで書いてみる
"""

n = int(input())
a = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(n, 1, -1):
    s[a[i - 2]] += 1 if s[i] == 0 else s[i] + 1
print(*s[1:], sep='\n')
