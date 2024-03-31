import io
import sys

# print(sys.getrecursionlimit())
_INPUT = """\
150
860 284
397 996
481 973
529 426
257 308
770 955
858 574
268 891
905 659
521 14
290 700
864 329
569 774
152 841
548 670
838 815
912 87
777 360
59 851
594 462
978 711
705 534
757 64
63 53
236 938
91 561
259 626
170 538
999 126
376 591
810 964
526 981
410 798
535 728
395 708
333 856
590 719
375 208
382 790
340 613
340 2
530 351
439 526
2 828
44 459
300 907
31 980
29 26
759 162
437 303
55 787
638 514
53 68
46 114
395 716
71 732
292 844
584 305
521 619
402 821
398 220
55 375
675 399
484 33
178 356
532 929
144 960
793 772
430 865
692 818
431 707
414 674
819 760
527 653
863 698
422 504
762 698
808 479
534 3
423 715
700 125
557 545
20 1000
218 537
75 372
313 985
457 463
365 866
399 477
205 51
484 719
363 766
666 813
307 335
513 208
495 417
140 115
225 731
397 516
665 409
402 430
217 649
446 848
696 307
224 823
177 258
305 3
526 329
654 116
268 160
936 529
228 853
260 866
838 691
53 543
28 32
984 775
889 746
382 91
413 691
595 522
61 667
105 242
258 346
927 794
624 337
995 647
315 102
901 22
858 738
13 692
238 741
388 305
817 307
458 793
486 15
968 875
863 36
967 493
463 539
493 662
910 83
253 343
212 410
564 332
624 77
659 468
945 707
498 227
952 2
"""
sys.stdin = io.StringIO(_INPUT)
"""
二次元平面上に N 個の都市があり、1 から N までの番号が付けられています。
都市 i は座標(Xi ,Yi​) にあり、都市i から都市j までの距離は３平方の定理です。
都市 1 から出発し、すべての都市を一度ずつ通った後、都市 1 へ戻ってくる経路のうち、合計距離ができるだけ短いものを出力してください。
"""
N = int(input())
X = [None] * N
Y = [None] * N
for i in range(0, N):
    X[i], Y[i] = map(int, input().split())


# 巡回セールスマン問題
# 最近傍法で
# ２座標の距離を求める関数
def calcDistance(x1, x2, y1, y2) -> float:
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


CONST_MAX_DISTANCE = 10000000
#allGraph = [[CONST_MAX_DISTANCE for j in range(N)] for i in range(N)]
visited = [False] * N
allDistanceList = []

# 全都市間を求めてしまう
for i in range(N):
    for j in range(N):
        distance = CONST_MAX_DISTANCE
        if i < j:
            # デバッグのため精度を少し落とす場合はroundで丸める
            distance = calcDistance(X[i], X[j], Y[i], Y[j])
            #allGraph[i][j] = distance
            allDistanceList.append([i, j, distance])

#for i in range(N):
#    print(allGraph[i])
# 距離順にソートしておく
allDistanceList.sort(key=lambda x: x[2])
#for i in allDistanceList:
#    if i[0] == 103 or i[1] == 103:
#        print(i)

# allDistanceListから一番短いルートを検索して繋げていく
route = []
visited[0] = True
nowCity = 0
route.append(nowCity)
print(nowCity + 1)
#while visitCount < N - 1:
while not all(visited):
    for cityDistance in allDistanceList:
        # 向き先が現在地を含んでいるか
        if cityDistance[0] == nowCity or cityDistance[1] == nowCity:
            # どっちが次の候補か求めておく
            if cityDistance[0] == nowCity:
                nextCandidate = cityDistance[1]
            else:
                nextCandidate = cityDistance[0]
            #print('nextCandidate', nextCandidate, 'visited', visited)
            # 訪問していなければ確定
            if not visited[nextCandidate]:
                # 移動しちゃいます
                nowCity = nextCandidate
                visited[nowCity] = True
                route.append(nowCity)
                print(nowCity + 1)
                #print('visitCount', visitCount)
                break
print(1)
