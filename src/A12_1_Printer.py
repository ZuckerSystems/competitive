import io
import sys

_INPUT = """\
11 800
1 2 3 4 5 1 7 8 9 11 99
"""
sys.stdin = io.StringIO(_INPUT)

# ここからが提出物
import collections

# 性能毎のプリンタークラスを作り出力数を算出させる
class Printer:
  performance = 0
  units = 0
  def __init__(self, performance, units):
    self.performance = performance
    self.units = units
  # ある秒数での出力枚数
  def getOutputCount(self, sec):
    # print((sec // self.performance) * self.units)
    return (sec // self.performance) * self.units
  def addUnit(self):
    self.units += 1
  
N, K = map(int, input().split())
A = list(map(int, input().split()))

printers = []
printerCountList = list(collections.Counter(A).items())

# 性能別のプリンタークラスを作成
for printerCount in printerCountList:
  # print(printerCount)
  printers.append(Printer(printerCount[0], printerCount[1]))

# 時間での2分探索してほしいのかもしれないがこのままでも通るので時間があれば
for sec in range(1, 10**10):
  output = 0
  for printer in printers:
    output = output + printer.getOutputCount(sec)
    #print(output)
  if output >= K:
    print(sec)
    break