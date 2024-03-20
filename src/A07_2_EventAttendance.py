
import io
import sys

_INPUT = """\
8
5
2 3
3 6
5 7
3 7
1 5
"""
sys.stdin = io.StringIO(_INPUT)

## 性能OK版

#### ここからが提出するプログラム
class Participant:
  startday = []
  endday = []
  increase = [] 
  # 各参加者の開始日と終了日を取得しておく。
  def __init__(self,startdays,enddays,days) -> None:
    self.startday = startdays
    self.endday = enddays
    # 無理やりな感じで1日の増減リストを作成しておく。最終日+1日のリスト
    self.increase = [0] * (days + 2)
    for i in range(len(startdays)):
      self.increase[startdays[i]] += 1
      self.increase[enddays[i] + 1] -= 1
    # print(self.increase)
  # その日の参加者を増減を返す
  def getTodayIncrease(self, day):
    # self.increase(day)がその日に参加する加減。
    # startday.count(day)が美しいと思ったが内部的にループ処理になりだめらしい
    # return int(self.startday.count(day) - self.endday.count(day - 1))
    return int(self.increase[day])

D = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N

for i in range(0, N):
  L[i], R[i] = list(map(int,input().split()))

participant = Participant(L, R, D)

participantCount = [ 0 ] * (D + 1)

for day in range(1, D + 1):
  #前日参加者とクラスが算出した当日参加者の増減を加算。
  participantCount[day] = participantCount[day - 1] + participant.getTodayIncrease(day)
  # print(str(day) + '日目')
  # print('参加者:'+ str(participant.getTodayIncrease(day)))
  print(participantCount[day])
  
