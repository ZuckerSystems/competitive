import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
3
BBB
"""
sys.stdin = io.StringIO(_INPUT)

# 右側は右から3番目までしか色を塗れない模様
# 右側の石のパターンと３連続型で解答が決まるのでは？
N = int(input())
S = [0] * N
S = list(input())

#print(S)
lastThree = S[N - 3] + S[N - 2] + S[N - 1]
#print('last3', lastThree)
ans = 'No'
if N == 3:  # RRR BBBのときにWAになったので付け足したが、そもそも３連続があればYesかも
    if lastThree == 'RRR' or lastThree == 'BBB':
        ans = 'Yes'
elif (lastThree != 'RRR' or lastThree != 'BBB'):
    ans = 'No'
    for i in range(N - 3):
        tmp = S[i] + S[i + 1] + S[i + 2]
        # print(tmp)
        if tmp == 'RRR' or tmp == 'BBB':
            ans = 'Yes'
            break

print(ans)
