import io
import sys

_INPUT = """\
5 3
2 3 16
3 5 23
1 2 22
"""
sys.stdin = io.StringIO(_INPUT)

# 労働時間算出クラス


class WorkPlan:
    endDayDict = dict()
    workingTimeStack = []
    todayhour = 24

    def __init__(self):
        self.endDayDict = dict()
        self.workingTimeStack = []
        self.todayhour = 24

    def addWorkPlan(self, endDay, hour):
        # 時間を追加する
        self.workingTimeStack.append(hour)
        # print('addWorkPlan', self.workingTimeStack)
        # 終了日とその時間リストを作成する
        if endDay in self.endDayDict:
            tmp = self.endDayDict[endDay].copy()
            tmp.append(hour)
            self.endDayDict[endDay] = tmp
        else:
            self.endDayDict[endDay] = [hour]
        self.todayhour = min(self.workingTimeStack)

    def getToDayhour(self) -> int:
        return self.todayhour

    def endDayRemove(self, endDay):
        # print('endDayRemove start', self.workingTimeStack)
        if endDay in self.endDayDict:
            for i in self.endDayDict[endDay]:
                self.workingTimeStack.remove(i)
        # print('endDayRemove end', self.workingTimeStack)
        self.todayhour = min(self.workingTimeStack + [24])


# 開始日が来たものを労働時間算出クラスに移動する
D, N = map(int, input().split())
LRH = [[0, 0, 0] for i in range(N)]
for i in range(N):
    LRH[i] = list(map(int, input().split()))

# LRHをLでソート
LRH.sort(key=lambda x: x[0])
# LRH.sort(key=lambda x: x[2])
# sorted(LRH, key=lambda x: x[2])

workPlan = WorkPlan()
step = 0
ans = 0
for day in range(1, D + 1):
    # print('a')
    while step < N:
        # print('b', LRH[step][0], day)
        if LRH[step][0] == day:
            # print('c')
            endDay = LRH[step][1]
            hour = LRH[step][2]
            workPlan.addWorkPlan(endDay, hour)
        elif LRH[step][0] > day:
            # print('d')
            break
        # print('e')
        step += 1
    # print('f')
    # 今日の労働時間を加算
    ans += workPlan.getToDayhour()
    # print('ans', ans)
    # 算出が終わったら今日終了分を消す
    workPlan.endDayRemove(day)

print(ans)
