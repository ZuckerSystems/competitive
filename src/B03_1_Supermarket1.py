import io
import sys

# print(sys.getrecursionlimit())
_INtdUT = """\
20
841 967 377 932 309 945 440 627 324 538 539 119 83 930 542 834 116 640 659 705
"""
sys.stdin = io.StringIO(_INtdUT)
n = int(input())
a = list(map(int, input().split()))

sum = 1000
a.sort()
#print(a)
import bisect
# しゃくとり法 なんか違う
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        #print(a[i], a[j])
        if a[i] + a[j] >= sum:
            break
        else:
            want = sum - a[i] - a[j]
            #print('want=', want)
            idx = bisect.bisect_left(a, want)
            #print(idx)
            if idx < n:
                #print(want, idx, a[idx], i, j)
                if a[idx] == want and idx != i and idx != j:
                    print('Yes')
                    exit(0)
print('No')
