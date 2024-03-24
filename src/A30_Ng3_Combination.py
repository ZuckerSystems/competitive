
import io
import sys

_INPUT = """\
7777 4444
"""
sys.stdin = io.StringIO(_INPUT)

def factorial_recursive(n: int) -> int:
    if n == 0: return 1
    return n * factorial_recursive(n - 1)

# n!/r!*(n-r)!
# この数は素数の積に変換可能
# 素数の積の減算後に掛け算する

# step1 素数リスト作成
# step2 素数毎の乗算数を算出
# step3 素数のみの乗算-乗算で割り算を実現
# step4 素数で割った値を算出
# 結果はTLE

# 素数リストの算出
# 素数列挙は数学の永遠のテーマのため高速算出アルゴリズムはライブラリを使うのがよい。
# これは貼り付け（https://ebisuke33.hatenablog.com/entry/eratosthenes）
def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

# 数値を素数の掛け算に変換する
def convertPrimeDict(primeNumberList: list, num: int, primeCountDict:dict) -> dict:
    n = num
    q = 0
    r = 0
    val = 0
    for primeNumber in reversed(primeNumberList):
        # print(primeNumber)
        q, r = divmod(n, primeNumber)
        while r == 0:
            # 素数の累計に商を加算
            # print(skipmemo)
            val = primeCountDict.get(primeNumber, 0)
            primeCountDict[primeNumber] = val + 1
            # print('素数:'+ str(primeNumber) + ':' + str(q))
            n = q #商がまた割れればループ継続
            q, r = divmod(n, primeNumber)

        # dictはミュータブルらしいのでreturn戻しだけかな？
    return

n, r = map(int, input().split())
# 割る数
CONST_DIVISION = 10 ** 9 + 7
# print(CONST_DIVISION)
primeNumberListN = sieve_of_eratosthenes(n)
# print(primeNumberListN)

primeNumberListR = sieve_of_eratosthenes(r)
primeNumberListNR = sieve_of_eratosthenes(n-r)
nDict = dict()
rDict = dict()

for num in range(2, n + 1):
    # print('num=' + str(num))
    convertPrimeDict(primeNumberListN, num , nDict)

# print(nDict)
for num in range(2, r + 1):
    convertPrimeDict(primeNumberListN, num , rDict)

# print(rDict)
for num in range(2, n - r + 1):
    convertPrimeDict(primeNumberListNR, num , rDict)

# print(rDict)

for dictKey in rDict:
    if dictKey in nDict:
        # 同じ素数の積を減算することで除算を行う
        if rDict[dictKey] <= nDict[dictKey]:
            nDict[dictKey] = nDict[dictKey] - rDict[dictKey]
            rDict[dictKey] = 0
        else:
            # 分母側が残る場合 論理的にここは通らない
            print('分母あり')
            nDict[dictKey] = 0
            rDict[dictKey] = rDict[dictKey] - nDict[dictKey]

ncVal = 1
#print(nDict)
for dictKey in nDict:
    if int(nDict[dictKey]) != 0:
        ncVal *= dictKey ** nDict[dictKey]
# 再現性の確認
#print(ncVal, factorial_recursive(n))

rcVal = 1
for dictKey in rDict:
    if int(rDict[dictKey]) != 0:
        rcVal *= dictKey ** rDict[dictKey]

#print(rcVal)
print(int(ncVal) % CONST_DIVISION)
