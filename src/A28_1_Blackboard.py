
import io
import sys

_INPUT = """\
4
+ 57
+ 43
* 100
- 1
"""
sys.stdin = io.StringIO(_INPUT)

# ここから提出
def A28calculator(command, val, beforVal):
    if command == "+":
        beforVal += val
    elif command == "-":
        beforVal -= val
    elif command == "*":
        beforVal *= val
    # 変数値が大きくなりすぎるのを防ぐため100*100で割った値を保持する
    return beforVal % 10000

N = int(input())
answer = 0
T: str
A: str
for i in range(N):
    T , A = input().split()
    answer = A28calculator(T, int(A), answer)
    print(answer)

