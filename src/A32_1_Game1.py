
import io
import sys

_INPUT = """\
15 2 3
"""
sys.stdin = io.StringIO(_INPUT)

# 入力など
N, A, B = map(int, input().split())

# N 個の石が積まれた山があり、 2 人のプレイヤーが交互に石を取り合います。
# 各プレイヤーは 1 回のターンで、以下のいずれかの操作をすることができます。
# 山から A 個の石を取り除く。
# 山から B 個の石を取り除く。


# この範囲は手番の勝ち?
# 最後の手番の人はAorB個固定で取らないといけないのか
# AorB以下で取っていいのか＝0個にすれば勝ち
winNo = A + B - 1
# print(winNo)
ans = 'Second'  # 初期値後手勝ち

# DPもらうDP的な動き
dp = [0] * (N+1)
# 1 勝ち 2>= 負け

# 勝てる位置を1に書き換えていく→N個目がどちらになるか判定
for i in range(N+1):
    # print(i)
    if i >= A and (dp[i - A] == 2 or dp[i - A] == 0):
        # print('A 1')
        dp[i] = 1
    elif i >= B and (dp[i - B] == 2 or dp[i - B] == 0):
        # print('B 1')
        dp[i] = 1
    else:
        dp[i] = 2

print(dp)
if dp[N] == 1:
    ans = 'First'
print(ans)
