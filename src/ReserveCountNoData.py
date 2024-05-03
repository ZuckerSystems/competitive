import io
import sys

# 15000件くらいのインプットデータを処理して空き枠数を求めるサンプル
# 大量の予約から空きを求めるようなお題の競プロ的な解答
# 計算量の測定目的.
# インプット１行目でクエリー
# ２行目以降が時間帯に埋まっている日付、枠番号、時間帯、ステータス（未使用）
#
# python m1 mac で0.05sec程度
#
_INtdUT = """\
20240423 20240429 30
20240424 0 900 930 1
20240424 1 900 1000 1
"""
"""
入力１行目にしてされた日付の期間に、指定された時間の空き枠が何分あるか算出する。
0900 2000 まで30分刻みとする。
同じ時間に複数の予約が取られることはない

15000件の予約数で 0.04秒(CPU m1 mac)
計算量は15000*6くらいで瞬殺可能な処理
"""

sys.stdin = io.StringIO(_INtdUT)
import time
import numpy as np
import datetime

np.set_printoptions(threshold=4800)
start = time.time()  # 現在時刻（処理開始前）を取得

inData = []
for l in sys.stdin:
    inData.append(l)


# 時間からインデックスに変換 0-index
def getTimeIndex(intTime):
    hh = intTime // 100
    mi = intTime % 100
    return (hh * 2 + mi // 30)


# データ取得条件を取得
STARTDATE, ENDDATE, TIME = map(int, inData[0].split())

startDate = datetime.datetime.strptime(str(STARTDATE), '%Y%m%d')
endDate = datetime.datetime.strptime(str(ENDDATE), '%Y%m%d')

weekDict = dict()

#マスタから日毎時間帯の総予約枠数
# ここは仮実装
dateTimeFrame = [[100] * 48] * 7  #実際は日付キーのdictに入れておくのがよい
MAXFRAME = 1000

# 期間分のスケジューラ作成 ここは予約数が知りたいだけなのでマスタとあっていなくてもよい。MAXFRAMEは十分大きい値でも可
for i in range((endDate - startDate).days + 1):
    ymd = startDate + datetime.timedelta(i)
    weekDict[ymd.strftime('%Y%m%d')] = np.zeros((48, MAXFRAME), int)

#print(weekDict.keys())

# データをschedulerに設置
for i in range(1, len(inData)):

    reserveData = list(map(int, inData[i].split()))
    #print(reserveData)
    # schedulerの取り出し
    scheduler = weekDict[str(reserveData[0])]
    startIdx = getTimeIndex(reserveData[2])
    endIdx = getTimeIndex(reserveData[3])

    # 終了時間まで1を全て入れる処理にした方が早いかも 長ーい予約の割合による
    # 累積和を取るやり方では１予約あたり２点のリスト座標探索更新＋累積和取得が必要
    # 全て最初に1を埋めれば累積和は不要になるが、１予約あたりのリスト座標更新の計算量がデータに依存する
    # 加算箇所 1は入り得ない -1が入っていたら連続して予約されているため0に変更する
    # [reserveData[1]]は枠番号
    if scheduler[startIdx][reserveData[1]] == 0:
        scheduler[startIdx][reserveData[1]] = 1
    elif scheduler[startIdx][reserveData[1]] == -1:
        scheduler[startIdx][reserveData[1]] = 0

    # 減算箇所 1が入っていたら連続して予約されているため0に変更する
    if scheduler[endIdx][reserveData[1]] == 0:
        scheduler[endIdx][reserveData[1]] = -1
    elif scheduler[endIdx][reserveData[1]] == 1:
        scheduler[endIdx][reserveData[1]] = 0
    #print(scheduler)


def calcTime(idx):
    hh = (idx // 2) * 100
    min = (idx % 2) * 30
    return hh + min


# schedulerの累積和計算
# 要求する時間による加工処理
for day, scheduler in weekDict.items():
    # 累積和縦方向
    scheduler = np.cumsum(scheduler, axis=0)

    frame = TIME / 30
    if frame > 1:
        #30分枠以上の場合埋まっている枠の上は埋まっている扱いとする必要あり
        for i in range(48):
            for j in range(100):
                if scheduler[i][j] == 1:
                    cnt = 1
                    while cnt < frame:
                        if scheduler[i - cnt][j] == 0:
                            scheduler[i - cnt][j] = 1
                        cnt += 1

    #print('cumsum')
    #print(scheduler)
    reserved = np.count_nonzero(scheduler == 1, axis=1)
    print(day)
    for i, x in enumerate(reserved):
        count = x
        # 予約枠を超える予約をカット
        if dateTimeFrame[0][i] < x:
            count = dateTimeFrame[0][i]
        print(calcTime(i), str(count) + '/' + str(dateTimeFrame[0][i]))
    #print('-------------------------------------------')

end = time.time()  # 現在時刻（処理完了後）を取得
time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用
