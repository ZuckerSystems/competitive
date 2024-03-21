
import io
import sys

_INPUT = """\
5
2 4 1 3
5 3 3
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
# 
# 動的計画法(DP)で算出する。
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ 0 ] * (N + 1)
dp[1] = 0
dp[2] = A[0] # 2部屋目に到着するのはA側のみ
aroute = 0
broute = 0
# 3部屋目以降に到着するのがAルートかBルートか早いのを算出する
for i in range(3, N + 1):
	aroute = dp[i - 1] + A[i - 2]
	broute = dp[i - 2] + B[i - 3]
	if aroute <= broute:
		dp[i] = aroute
	else:
		dp[i] = broute

# 辿ってきたルートを逆算する
route = []
room = N
# print(dp)
while room >= 1:
	# print(room)
	route.append(room)

	# 1,2の部屋の処理は初期値設定しているためDPが正しくなく別処理が必要
	if room == 1:   #この場合1の部屋まで終わっている
		break
	if room == 2:
		route.append(1)
		break
	# 逆の条件でroomの算出
	aroute = dp[room - 1] + A[room - 2]
	broute = dp[room - 2] + B[room - 3]
	if aroute <= broute:
		#ルートAを通ったはず 指定されたマイナス分部屋を戻って再帰的に処理
		room -= 1
	else:
		#ルートBも同様
		room -= 2
#print(dp)
#print(dp[N])
print(len(route))
route.reverse()
print(*route)

